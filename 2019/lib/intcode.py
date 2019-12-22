"""
Multiple puzzles this year use "intcode" this library will be used to work with those codes
"""

"""
define possible operation codes, and corresponding operations -
note: writing the dictionary out would have been clearer actually
"""

# TODO: figure out how to do this




class fixed_input:
    def __init__(self, data):
        self.data = data
        self.pointer = 0
    def next(self):
        entry = self.data[self.pointer]
        self.pointer += 1
        if self.pointer >= len(self.data):
            self.pointer = 0
        return entry

class int_computer():
    """
    operates on intcodes per Advent of Code 2019 - Day 2
    """
    OP_KEY = {
        1: (self.debug, 4),
        2: (self.debug, 4),
        3: (self.debug, 2),
        4: (self.debug, 2),
        88: (self.debug, 1),
        99: (self.terminate, 0)
    }
    def __init__(self, code):
        self.code = code
        self.pointer = 0

    def terminate(self):
        return 0

    def run_code(self):
        status = 1
        while status == 1:
            status = self.intcode_operation()

    def intcode_operation(self):
        """ handle the operation """
        opcode, arglist = self.intcode_blk_parse()
        retVal = self.OP_KEY[int(opcode)][0]()
        self.pointer += self.OP_KEY[int(opcode)][1]
        return retVal

    def debug(self, args):
        print("opcode: {}".format(self.code[self.pointer]))
        print("Param 1: {}, Arg: {}".format(self.code[self.pointer+1], args[0]))
        print("Param 2: {}, Arg: {}".format(self.code[self.pointer+2], args[1]))
        print("Param 3: {}, Arg: {}".format(self.code[self.pointer+3], args[2]))
        return 1

    def intcode_blk_parse(self):
        """ get opcode and arglist from current memory location """
        cur_point = self.pointer
        raw_opcode = self.code[cur_point]
        opcode = int(raw_opcode[-2:])
        raw_arglist = raw_opcode[:-2]
        arglist = [int(x) for x in raw_arglist]
        if arglist == None:
            arglist = [0]
        arglist.reverse()
        while len(arglist) < 3:
            arglist.append(0)

        return opcode, arglist


if __name__ == "__main__":
    def test_opcode_parser():
        opcode_parse_tests1 = ['88', '188', '1088', '1188', '10088',
                               '10188', '11088', '11188', '99']
        opcode_parse_tests2 = ['8', '108', '1008', '1108', '10008',
                               '10108', '11008', '11108', '99']
        tester = int_computer(opcode_parse_tests2)
        print(tester.code)
        tester.run_code()
        print(tester.code)

    test_opcode_parser()


    
