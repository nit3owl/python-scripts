def get_random_code(size):
    return ''.join(random.choice(alphanumeric) for _ in range(size))

def generate_codes(num, size, random):
    filename = 'output_' + time.strftime("%H%M%S") + '.csv'
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

def main():
    parser = argparse.ArgumentParser(description='Generate a .csv file with N codes of Y length.')
    parser.add_argument('num', metavar='N', type=int, help='number of codes to generate')
    parser.add_argument('size', metavar='S', type=int, help='length of codes')
    parser.add_argument('-r', metavar='--random', action='store_const', const=True, default=False, dest='random', required=False, 
            help='request pseudo-random, unique (per exec) codes')
    args = parser.parse_args()
    if not args.random:
        if args.num > (args.size * 10):
            print  ("ERROR: Cannot generate unique codes becuase num codes requested must be " +
                    "less than or equal to requsted code size x 10")
            print  ("num was '" + str(args.num) + "' but max num for code size '" + str(args.size) + 
                    "' is '" + str((args.size * 10)) + "'")
            sys.exit(1)
    else:
        maxcodes = args.size**len(alphanumeric)
        if args.num > maxcodes:
            print  ("ERROR: Cannot generate unique \"random\" codes becuase num codes requested must be " +
                    "less than or equal to requsted code size x " + str(len(alphanumeric)))
            print  ("num was '" + str(args.num) + "' but max num for code size '" + str(args.size) + 
                    "' is '" + str(maxcodes) + "'")
            sys.exit(1)
    filename = generate_codes(args.num, args.size, args.random)
    print ("Generation complete, codes ouput in %s" % filename)

import argparse
import random
import string
import sys
import time
alphanumeric = string.ascii_uppercase + string.digits
main()
