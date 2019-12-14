"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""

# TODO: figure out how to do this
OP_DICT = {
    1: intcode_add,
    2: intcode_mult,
    3: intcode_get_input,
    4: intcode_get_output
    99: intcode_quit
}


def intcode_add(code, pointer, argstring=(0, 0, 0), data_stream=None):
    """
    moves pointer 4 positions forward, adds positions 1 and 2,
    outputs position 3
    """
    in1 = code[pointer+1]
    in2 = code[pointer+2]
    if not argstring[0]:
        in1 = code[in1]
    if not argstring[1]:
        in2 = code[in2]
    result = in1 + in2
    if not argstring[2]:
        code[pointer+2] = result
    else:
        out1 = code[pointer+2]
        code[out1] = result
    status = 1
    return code, status


def intcode_mult(code, pointer, argstring=(0, 0, 0), data_stream=None):
    """
    moves pointer 4 positions forward, adds positions 1 and 2,
    outputs position 3
    """
    in1 = code[pointer+1]
    in2 = code[pointer+2]
    if not argstring[0]:
        in1 = code[in1]
    if not argstring[1]:
        in2 = code[in2]
    result = in1 * in2
    if not argstring[2]:
        code[pointer+2] = result
    else:
        out1 = code[pointer+2]
        code[out1] = result
    status = 1
    return code, status


def intcode_get_input(code, pointer, argstring):
    status = 1
    return code, status


def intcode_get_output(code, pointer, argstring):
    status = 1
    return code, status


def intcode_exit(code, pointer, argstring, data_stream):
    return code, 0





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
        # intcode operations format:
        # intcode_op(code, pointer, argstring, datastream)
        self.code, status = OP_DICT[opcode](self.code, self.pointer,
                                            argstring, datastream)

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
