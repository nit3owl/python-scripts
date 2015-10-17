def get_random_code(size):
    return ''.join(random.choice(alphanumeric) for _ in range(size))

def generate_codes(num, size, random):
    filename = 'output_' + time.strftime('%H%M%S') + '.csv'
    output = open(filename, 'w')
    if not random:
        for i in range(0, num):
            temp = '%0' + str(size) + 'd' 
            temp = temp % (i,)
            output.write('%s,\n' % temp)
        output.write(temp)
    else:
        codes = set()
        while len(codes) < num:
            codes.add(get_random_code(size))
        
        for c in codes:
            output.write('%s,\n' % c)
    output.close()
    return filename

def positive_int(value):
    i = int(value)
    if i < 0:
        raise argparse.ArgumentTypeError('invalid positive int value: \'{0}\''.format(value))
    return i

def main():
    parser = argparse.ArgumentParser(description='Generate a .csv file with N unique codes of Y length.')
    parser.add_argument('num', metavar='N', type=positive_int, help='number of codes to generate')
    parser.add_argument('size', metavar='S', type=positive_int, help='length of codes')
    parser.add_argument('-r', metavar='--random', action='store_const', const=True, default=False, dest='random', required=False, 
            help='request pseudo-random, unique (per exec) codes')
    args = parser.parse_args()
    if not args.random:
        maxcodes = 10**args.size
        if args.num > maxcodes:
            print  ('ERROR: Cannot generate unique codes with iteration becuase num codes requested must be ' +
                    'less than or equal to 10^size')
            print  ('num was \'{0}\' but max num for code size \'{1}\' is \'{2}\''.format(str(args.num), str(args.size), maxcodes))
            sys.exit(1)
    else:
        maxcodes = math.factorial(len(alphanumeric)) / math.factorial(abs((len(alphanumeric) - args.size)))
        if args.num > maxcodes:
            print  ('ERROR: Cannot generate unique "random" codes becuase num codes requested must be ' +
                    'less than or equal to requsted code {0}!/({0} - size)!'.format(str(len(alphanumeric))))
            print  ('num was \'{0}\' but max num for code size \'{1}\' is \'{2}\''.format(str(args.num), str(args.size), maxcodes))
            sys.exit(1)
    filename = generate_codes(args.num, args.size, args.random)
    print ('Generation complete, codes ouput in {0}'.format(filename))

import argparse
import math
import random
import string
import sys
import time
alphanumeric = string.ascii_uppercase + string.digits
main()
