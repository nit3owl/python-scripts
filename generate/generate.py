def get_random_code(size):
    return ''.join(random.choice(alphanumeric) for _ in range(size))

def generate_codes(num, size, random):
    output = open('output.csv', 'w')
    if not random:
        for i in range(0, num):
            temp = '%0'+str(size)+'d' 
            temp = temp % (i,)
            output.write('%s,\n' % temp)
    else:
        for i in range(0, num):
            output.write('%s,\n' % get_random_code(size))
    output.close()

def main():
    parser = argparse.ArgumentParser(description='Generate a .csv file with N codes of Y length.')
    parser.add_argument('num', metavar='N', type=int, help='number of codes to generate')
    parser.add_argument('size', metavar='S', type=int, help='length of codes')
    parser.add_argument('-r', metavar='--random', action='store_const', const=True, default=False, dest='random', required=False, 
            help='request pseudo-random, unique (per exec) codes')
    args = parser.parse_args()
    generate_codes(args.num, args.size, args.random)
    print "Generation complete, codes ouput in output.csv."

import argparse
import string
import random
alphanumeric = string.ascii_uppercase + string.digits
main()
