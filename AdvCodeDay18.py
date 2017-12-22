class Program():
    def __init__(self,instructions):
        self.instructions = instructions
        self.ptr = 0
        self.reg = {}
        self.msg_queue = []
        self.other_program = None
        self.wait = False
        self.sent_value = 0

    def set_other_program(self,other_program):
        self.other_program = other_program

    def add_to_queue(self,message):
        self.msg_queue.append(message)

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
        if x not in self.reg:
            self.reg[x] = 0
        inc_ptr = True
        if instruction == 'snd':
            self.other_program.add_to_queue(self.reg[x])
            self.sent_message += 1
        elif instruction == 'rcv':
            if len(self.msg_queue) > 0:
                cur_msg = self.msg_queue.pop(0)
                self.reg[x] = cur_msg
            else:
                inc_ptr = False
        else:
            y = self.get_reg_or_int(cur_ins[2])
            if instruction == 'set':
                self.reg[x] = y
            elif instruction == 'add':
                self.reg[x] += y
            elif instruction == 'mul':
                self.reg[x] *= y
            elif instruction == 'mod':
                self.reg[x] %= y
            elif instruction == 'jgz':
                if self.reg[x] != 0:
                    self.ptr += y
                    inc_ptr = False
        if inc_ptr:
            self.ptr += 1

    def read_instructions(self):
        ins_ctr = 0
        if self.ptr >= start and self.ptr < end and not self.wait:           
            self.read_instruction()
            ins_ctr += 1
        return ins_ctr

ins_list = []
file = 'Adv18Input.txt'
with open(file,'r') as f:
    for row in f.readlines():
        ins_list.append(row.strip())

##ins_list = ['set a 1','add a 2','mul a a','mod a 5','snd a','set a 0','rcv a','jgz a -1','set a 1','jgz a -2']
##p = Program(ins_list)
##part_one = p.read_instructions()
p1 = Program(ins_list)
p2 = Program(ins_list)
p1.set_other_program(p2)
p2.set_other_program(p1)
brk = False
while not brk:
    #run program 1 until terminates
    p1_i = p1.read_instruction()
    while p1_i > 0:
        p1_i = p1.read_instruction()
    p2_i = p2.read_instruction()
    while p2_i > 0:
        p2_i = p2.read_instruction()
