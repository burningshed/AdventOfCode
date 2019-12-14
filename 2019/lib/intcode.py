"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""

# TODO: figure out how to do this







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
        self.OP_DICT = {
            1: self.intcode_add,
            2: self.intcode_mult,
            3: self.intcode_get_input,
            4: self.intcode_get_output,
            99: self.intcode_quit
        }
 
    def intcode_add(self, argstring=(0, 0, 0)):
        """
        moves pointer 4 positions forward, adds positions 1 and 2,
        outputs position 3
        """
        STEP_SIZE = 4
        in1 = int(self.code[self.pointer+1])
        in2 = int(self.code[self.pointer+2])
        if not argstring[0]:
            in1 = int(self.code[in1])
        if not argstring[1]:
            in2 = int(self.code[in2])
            result = in1 + in2
        if not argstring[2]:
            out1 = int(self.code[self.pointer+2])
            self.code[out1] = str(result)
        else:
            self.code[self.pointer+2] = str(result)
        self.pointer += STEP_SIZE
        return 1

    def intcode_mult(self, argstring):
        """
        moves pointer 4 positions forward, multiplies positions 1 and 2,
        outputs position 3
        """
        STEP_SIZE = 4
        in1 = int(self.code[self.pointer+1])
        in2 = int(self.code[self.pointer+2])
        if not argstring[0]:
            in1 = int(self.code[in1])
        if not argstring[1]:
            in2 = int(self.code[in2])
            result = in1 * in2
        if not argstring[2]:
            out1 = int(self.code[self.pointer+2])
            self.code[out1] = str(result)
        else:
            self.code[self.pointer+2] = str(result)
        self.pointer += STEP_SIZE
        return 1

    def intcode_get_input(self, argstring):
        status = 1
        return status

    def intcode_get_output(self, argstring):
        status = 1
        return status

    def intcode_quit(self, argstring):
        return 0

   
    def run_step(self):
        """
        perform one operation,
        """
        instruction_str = self.code[self.pointer]
        opcode = instruction_str[-2:]
        # define argstring here
        # default
        argstring = (0, 0, 0)
        status = self.OP_DICT[int(opcode)](argstring)
        return status

    def run_code(self):
        """
        run through intcode, if no code is provided use the code provided when class was created
        returns 0 if 99 was reached, 2 if some unexpected op-code encountered
        """
        retVal = 1
        while(retVal == 1):
            retVal = self.run_step()
        return retVal

    def get_code(self):
        return self.code


if __name__ == "__main__":
    testCase2 = int_computer(
        ["1", '9', '10', '3', '2', '3', '11', '0', '99', '30', '40', '50'])
    testCase1 = int_computer(["1", "1", "1", "1", "99"])
    print(testCase1.get_code())
    print(testCase1.run_code())
    print(testCase1.get_code())
    #testCase.run_step()
