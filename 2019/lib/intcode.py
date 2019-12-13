"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""

# TODO: figure out how to do this
OP_DICT = {
    1: intcode.add,
    2: intcode.mult,
    3: intcode.get_input,
    4: intcode.get_output
}

def intcode_add(code, pointer, argstring):
    """
    adds 
    """



class int_computer():
    """
    operates on intcodes per Advent of Code 2019 - Day 2
    """
    def __init__(self, init_code):
        """
        Initialize with some intcode
        """
        self.code = init_code
        self.pointer = 0

    def run_step(self):
        """
        perform one operation,
        """
        instruction_str = self.code[self.pointer]
        opcode = instruction_str[-2:]
        print(opcode)

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
    testCase = int_computer(
        ["1", '9', '10', '3', '2', '3', '11', '0', '99', '30', '40', '50'])
    #print(testCase.get_code())
    #print(testCase.run_code())
    #print(testCase.get_code())
    testCase.run_step()
