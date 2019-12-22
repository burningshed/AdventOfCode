puz_sol = intcode.int_computer(puz_in, intcode.diag_print)
    puz_sol.run_code()

def day5p1_diag2(puz_in):
    stream = intcode.fixed_input('1')
    puz_sol = intcode.int_computer(puz_in, stream)
    print(puz_sol.run_code_d2())

day5p1_diag(code)
