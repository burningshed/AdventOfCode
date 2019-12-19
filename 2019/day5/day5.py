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
    puz_sol.run_code()
    return puz_sol.get_code()
print(day5p1(code))