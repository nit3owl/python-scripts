# [python-scripts](https://github.com/nit3owl/python-scripts)

## Scripts

### generate

This script will generate a .csv with N "codes" of Y length. The generated codes will be unique (per execution). If the -r flag
is specified, the codes will be "random" alphanumeric strings. Otherwise, the codes are strings from 0 to N with 0's prepended
to make each code the length requested, eg - "0000", "0001", "0002", etc.

Uniqueness is guaranteed for non-random codes through iteration. For random codes, it is guaranteed via the use of a set to hold
generated codes before writing them to the output file. This has the possibility to take quite a while if there are many collisions,
but is relatively unlikely. Collisions are most prevalent when requesting near the total number of possible permutations for a given
length, eg - requesting 36 codes of length 1. An example runtime on a 64 bit Windows 10 machine with an i7 @ 1.7GHz is about 7
seconds to produce 500,000 twenty digit random codes.

Uniqueness is also enforced by bounds checks. That is, before code generation occurs, the input is validated to ensure that uniqueness
is possible for N codes of Y length. If it is not possible, a descriptive message is thrown to the user and execution halts.
Eg - the user asks for 11 non-random codes of length 1 but there are a maximum of 10 unique codes [0...9] at that length with simple
iteration. Therefore, execution will halt with an error message.
The formulas used are to determine the max number of codes are:
	non-random (simple iteration)   : 10^Y where Y is the requested code length
									  eg, Y = 2 can have codes from 00-99, or 100 codes
	random codes				    : 36! / (|36 - Y|)! where Y is the requested code length
								      eg, Y = 2 can have 1260 codes
													
### cc_script

This script takes two RAW files as input and finds entries in file1 that do not have duplicate primary key entries in file2

### busy

This script lets you show everyone how busy you really are, despite whatever they may think. It will print a variety of "random", "interesting" 
messages which indicate all the interesting work you're getting done; try running it on your most visible monitor.

The script allows some customization as to the level of busyness you feel you need to show the world.

###

This script calls a website to fetch air quality reports. The reports are parsed, "analyzed", and pretty-printed to screen.s