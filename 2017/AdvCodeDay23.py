from sympy import sieve

class Program():
    def __init__(self,instructions):
        self.instructions = instructions
        self.ptr = 0
        self.reg = {}
        self.instructions_read = {}

    def get_reg_or_int(self,param):
        try:
            x = self.reg[param]
        except:
            x = int(param)
        return x

    def read_instruction(self):
        cur_ins = self.instructions[self.ptr].split(' ')
##        print(cur_ins)
        instruction = cur_ins[0]
        x = cur_ins[1]
        try:
            x = int(x)
        except:
            pass
        if x not in self.reg and not isinstance(x,int):
            self.reg[x] = 0
        elif isinstance(x,int):
            self.reg[x] = 1
        inc_ptr = True
        y = self.get_reg_or_int(cur_ins[2])
        if instruction not in self.instructions_read:
            self.instructions_read[instruction] = 0
        self.instructions_read[instruction] += 1
        if instruction == 'set':
            self.reg[x] = y
        elif instruction == 'sub':
            self.reg[x] -= y
        elif instruction == 'mul':
            self.reg[x] *= y
        elif instruction == 'jnz':
            if self.reg[x] != 0:
                self.ptr += y
                inc_ptr = False
        if inc_ptr:
            self.ptr += 1

    def read_instructions(self):
        start = 0
        end = len(self.instructions)
        ins_ctr = 0
        while self.ptr >= start and self.ptr < end:           
            self.read_instruction()
            ins_ctr += 1
        return self.instructions_read['mul']

def part_two_fn():
    b = 105700
    c = 122700
##    sieve._reset()
    sieve.extend_to_no(c)
    h = 0
    for i in range(b, c + 1,17):
        if i not in sieve:
            h += 1
    return h

ins_list = []
file = 'Adv23Input.txt'
with open(file,'r') as f:
    for row in f.readlines():
        ins_list.append(row.strip())

p = Program(ins_list)
part_one = p.read_instructions()
part_two = part_two_fn()
