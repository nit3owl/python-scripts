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

def get_busy(busyness):
    sleepiness = (10 - busyness) * .225
    tasks = get_busy_tasks()
    
    while True:
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

    args = parser.parse_args()

    try:
        print('Becoming busy at level {0}...'.format(args.busyness_level))
        get_busy(args.busyness_level)
    except KeyboardInterrupt:
        print('\nBusyness interrupted; exiting...')
        sys.exit(0)

import argparse
import math
import random
import string
import time
import sys

main()
