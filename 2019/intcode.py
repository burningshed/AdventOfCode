"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""
import operator

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""
OP_CODES = (1,2)
OP_VALS = (operator.__add__,operator.__mul__)
OP_DICT = {OP_CODES[x]:OP_VALS[x] for x in range(len(OP_CODES))}


class int_computer():
    """
    operates on intcodes per Advent of Code 2019 - Day 2
    """
    def __init__(self, init_code):
        """
        Initialize with some intcode
        """
        self.code = init_code
    def run_step(self, start_block, code):
        """
        perform one operation, using the instruction set starting at start_block on provided code
        """
        if code[start_block] == 99:
            return 0
        if code[start_block] not in OP_DICT:
            return 2
        OP = OP_DICT[code[start_block]]
        in_val1 = code[code[start_block+1]]
        in_val2 = code[code[start_block+2]]
        out_loc = code[start_block+3]
        code[out_loc] = OP(in_val1, in_val2)
        return 1


    def run_code(self, code=None):
        """
        run through intcode, if no code is provided use the code provided when class was created
        returns 0 if 99 was reached, 2 if some unexpected op-code encountered
        """
        if code is None:
            code = self.code
        retVal = 1
        curLoc = 0
        while(retVal == 1):
            retVal = self.run_step(curLoc, code)
            curLoc += 4
        return retVal

    def get_code(self):
        return self.code

if __name__ == "__main__":
    testCase = int_computer([10,9,10,3,2,3,11,0,99,30,40,50])
    print(testCase.get_code())
    print(testCase.run_code())
    print(testCase.get_code())
