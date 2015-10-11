import linecache
from collections import OrderedDict

def compare_files(fn1, fn2):
    try:
        file1 = open(fn1, "r")
        file2 = open(fn2, "r")
    except:
        print "File(s) not found"
        sys.exit(1)
    
    output = open("output.txt", "w")
    file1_pairs = OrderedDict()
    file2_pairs = OrderedDict()
    unique_lines = []
    for columns in (raw.strip().split("|") for raw in file1):
        file1_pairs[columns[0] + columns[2]] = columns[2]
    file1.close()
    for columns in (raw.strip().split("|") for raw in file2):
        file2_pairs[columns[0] + columns[2]] = columns[2]
    file2.close()
    count = 0
    for key in file1_pairs:
        if key in file2_pairs:
            if not file1_pairs[key] == file2_pairs[key]:
                unique_lines.append(count)
        else:
            unique_lines.append(count)
        count += 1

    for i in unique_lines:
        line = linecache.getline("file1", i+1)
        output.write(line)

    output.close()

def main(args):
    try:
        fn1 = args[1]
        fn2 = args[2]
    except:
        print "Usage: %s <file1> <file2>" % sys.argv[0]
        sys.exit(1)    

    compare_files(fn1, fn2)

import sys
main(sys.argv)
