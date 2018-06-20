def get_busy_tasks():
    tasks = [
            'rejiggering the capacitor',
            '//set defcon 2 and alert general staff to quarters\nsetStatus(2);\nalertSecDef();',
            'performing calulcations:\na7e7fe3b2e6 * 344 073 147 051 313 161 170 075 323 175\n...\n...\n...',
            '0x01A0 six four do while not done doing..',
            'all work and no play makes jack a dull boy',
            'let x = 1;\nwhile x > 0;\n  if(x)\n    console.log(\'truthiness is the best kind of truth\');',
            'Notification Type: PROBLEM\nServoce: Swap 30 20\nHost: c12nite345.nit3owl.github.io\nAddress: c12nite345.nit3owl.github.io\State: WARNING\nSWAP WARNING - 28% free\nAdditional Info: http://c12nite345.nit3owl.github.io/nagiosxi/'
            ]

    return tasks

def fetch_todos():
    #there are currently 200 todo objects
    resource_id = str(random.randint(1, 200))
    todo = urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/" + resource_id).read()

    parsed = json.loads(todo.decode('utf8').replace("'", '"'))
    return "status: \n" + json.dumps(parsed, indent=4, sort_keys=False)

def get_busy(busyness, offline):
    sleepiness = (10 - busyness) * .225
    tasks = get_busy_tasks()
    last_http_call = int(time.time())

    while True:
        #time.time() returns time in seconds not milliseconds 
        current_time = int(time.time())
        if not offline and (current_time - last_http_call >= 10):
            last_http_call = current_time
            print('{0}: {1}'.format(random.randint(0, 100000000), fetch_todos()))
        else:
            task = random.choice(tasks)
            print('{0}: {1}'.format(random.randint(0, 1000000000), task))
        
        time.sleep(sleepiness + (random.randint(0, 1) * .31))

def positive_single_digit_int(value):
    i = int(value)
    if i < 0 or i > 9:
        raise argparse.ArgumentTypeError('Invalid: Expected digit 0-9, got {0}'.format(value))
    return i

def main():
    parser = argparse.ArgumentParser(description = 'Let everyone see how busy you really are')
    parser.add_argument('busyness_level', metavar='b', type=positive_single_digit_int, default=5, help='busyness level between 0 (not at all) and 9 (SUPER busy)')
    parser.add_argument('--offline', action="store_true", help='runs in "offline" mode and will not make external API calls for dummy data')

    args = parser.parse_args()

    try:
        start_message = 'Becoming busy at level {0}'.format(args.busyness_level)
        if args.offline:
            start_message += " and running offline"
        start_message += "...\n"

        print(start_message)
    
        get_busy(args.busyness_level, args.offline)
    except KeyboardInterrupt:
        print('\nBusyness interrupted; exiting...')
        sys.exit(0)

import argparse
import math
import random
import string
import time
import sys
import urllib.request
import json

main()
