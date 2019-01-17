import os
import subprocess
import calendar
import datetime
import argparse
import sys

def print_output(output_map, sorted):
    for key, value in output_map.items():
        print("{}: {} commits".format(key, value))

def check_and_pull():
    subprocess.call(['git', 'checkout', 'master'])
    subprocess.call(['git', 'pull'])

def count_commits_per_month(repos):
    commits_per_month = {}
    current_year = datetime.datetime.now().year

    for repo in repos:
        wd = os.getcwd()
        os.chdir(repo)

        check_and_pull()

        for i in range(1, 12):
            month = calendar.month_abbr[i]

            since = '--since="' + month + ' 1 ' + str(current_year) + '"'
            before = '--before="' + calendar.month_abbr[i + 1] + ' 1 ' + str(current_year) + '"'
            command = ['git', 'rev-list', '--count', since, before, '--all', '--no-merges']
            output, error = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            
            if month in commits_per_month:
                commits = commits_per_month[month]
                commits_per_month[month] = commits + int(output)
            else:
                commits_per_month[month] = int(output)

            #since the year has changed and we're being lazy, get the final month of the year
            month = calendar.month_abbr[12]

            since = '--since="' + month + ' 1 ' + str(current_year) + '"'
            before = '--before="' + calendar.month_abbr[i + 1] + ' 1 ' + str(current_year) + '"'
            command = ['git', 'rev-list', '--count', since, before, '--all', '--no-merges']
            output, error = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            
            if month in commits_per_month:
                commits = commits_per_month[month]
                commits_per_month[month] = commits + int(output)
            else:
                commits_per_month[month] = int(output)

            os.chdir(wd)

        print_output(commits_per_month, False)

def count_commits_per_user(repos):
    commits_per_user = {}
    current_year = datetime.datetime.now().year

    for repo in repos:
        wd = os.getcwd()
        os.chdir(repo)

        check_and_pull()

        command = ['git', 'shortlog', '-s', '-n', '--all', '--no-merges']
        output, error = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output.lstrip()
        output.rstrip()
        lines = output.split('\n')

        for line in lines:
            arr = line.split('\t')
            if len(arr) == 2:
                repo_commits = arr[0].lstrip()
                user = arr[1]

                if user in commits_per_user:
                    commits = commits_per_user[user]
                    commits_per_user[user] = commits + int(repo_commits)
                else:
                    commits_per_user[user] = int(repo_commits)
        
        os.chdir(wd)

    print_output(commits_per_user, True)

def get_directory_list(directory):
    return [directory]

def main():
    parser = argparse.ArgumentParser(description = 'Use git\'s logging to count commits')
    parser.add_argument('metric', nargs='?', help='user = count commits by user | month = count commits by month')
    parser.add_argument('--dir', nargs='?', help='root directory to search for git repos - defaults to current')
    #parser.add_argument('--author', nargs='?', help='counts commits pnly by the supplied author')

    args = parser.parse_args()

    try:
        if args.dir is None:
            directory = os.getcwd()
        else:
            directory = args.dir
        metric = args.metric
        if metric == 'user':
            count_commits_per_user(get_directory_list(directory))
        elif metric == 'month':
            count_commits_per_month(get_directory_list(directory))
        else:
            parser.print_help(sys.stderr)

    except KeyboardInterrupt:
        print('\nCaught interrupt; exiting...')
        sys.exit(0)

main()