def generate_codes(num, size):
    output = open('output.csv', 'w')
    for i in range(0, num):
        temp = "%0"+size+"d" 
        temp = temp % (i,)
        output.write("%s,\n" % temp) 
    output.close()

def main(args):
    try:
        num  = int(args[1])
        size = args[2]
    except:
        print "Usage: %s <numToGen> <lengthOfCodes>" % sys.argv[0]
        sys.exit(1)

    generate_codes(num, size)

import sys
main(sys.argv)
