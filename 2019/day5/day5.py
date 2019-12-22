"""
Advent of Code 2019 - Day 5
Update Intcode
Add opcodes:
3 (single integer input, store at location provided)
4 (outputs value stored at location)

Parameter Modes
mode 0 - parameters are position
mode 1 - immediate mode - parameters are values

first instruction is not PPPOO where Ps are parameter modes (one for each parameter) and Os are the 2 digit opcodes
"""
import intcode
PUZZLE_INPUT = "./day5.in"
input = open(PUZZLE_INPUT, 'r')
for line in input:
    code = line.split(',')

def day5p1(puz_in):
    stream = intcode.fixed_input('1')
    puz_sol = intcode.int_computer(puz_in, stream)
    print("Return Value: {}".format(puz_sol.run_code()))


def day5p1_diag(puz_in):
    puz_sol = intcode.int_computer(puz_in, intcode.diag_print)
    puz_sol.run_code()

def day5p1_diag2(puz_in):
    stream = intcode.fixed_input('1')
    puz_sol = intcode.int_computer(puz_in, stream)
    print(puz_sol.run_code_d2())

day5p1_diag(code)
