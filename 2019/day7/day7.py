"""
Advent of Code 2019 - Day 7 - Aplification Circuit

plan:
p. implement ability to take input
1. function taking phase settings as input
    - create 5 instances of int_computer
    - run through with phase settings
2. build loop to test all possible combinations
"""
# IMPORT statements
import intcode
import itertools


def thrust_prog(code, term):
    # taking code amd term supplied execute intcode
    sig = '0'
    for phase in term:
        # create input
        in_stream = [phase, sig]
        in_func = None
        # create output
        store = intcode.stored_out()
        # create int_computer
        amp = intcode.int_computer(code, store.print_func, in_func)
        amp.run_code()
        sig = store.get(0)
    return sig


#########################
#
# BEGIN Input Handling
#
########################

# Get your puzzle input, and save the file to your computer
# add the path "C:/PATH/to/File.txt" <- Windows or "/PATH/to/File" <- Unix here
FILE_PATH = "./day7.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')
for line in RawInput:
    code = line.split(',')


testcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
testcode = [str(x) for x in testcode]
testterm = ['1', '0', '4', '3', '2']
testthrust = 65210

# replace real code with testcode, prevents accidently running full code while testing
code = testcode

# code to test each permutation of 01234
def day7(code):
    max_thrust = 0
    for term in itertools.permutations('12340'):
        cur_thurst = thrust_prog(code, term)
        if cur_thrust > max_thrust:
            max_thrust = cur_thurst
            best_term = term
    return max_thrust, best_term

def day7test(code, term, expected_thrust):
    return thrust_prog(code, term) == expected_thrust

#print(day7test(testcode, testterm, testthrust))

#print(day7(code))
