def spin(l,x):
    return l[-x:] + l[:-x]

def exchange(l,x,y):
    l[x],l[y] = l[y],l[x]
    return l

def partner(l,a,b):
    a_ind = l.index(a)
    b_ind = l.index(b)
    l[a_ind],l[b_ind] = l[b_ind],l[a_ind]
    return l

def read_instruction(l,instr):
    c = instr[0]
    if c=='s':
        rest = instr[1:]
        size = int(rest)
        l = spin(l,size)
    elif c=='x':
        rest = instr[1:]
        r = rest.split('/')
        ind_1 = int(r[0])
        ind_2 = int(r[1])
        l = exchange(l,ind_1,ind_2)
    elif c=='p':
        rest = instr[1:]
        r = rest.split('/')
        char_1 = r[0]
        char_2 = r[1]
        l = partner(l,char_1,char_2)
    return l

def part_one_ex_fn(instruction_list):
    l = ['a','b','c','d','e']
    for instruction in instruction_list:
        l = read_instruction(l,instruction)
##        print(''.join(l))
    return ''.join(l)

def part_one_fn(instruction_list):
    l = [chr(i) for i in range(97,113)]
    for instruction in instruction_list:
        l = read_instruction(l,instruction)
##        print(''.join(l))
    return ''.join(l)

##instruction_list = ['s1','x3/4','pe/b']
##part_one_ex = part_one_ex_fn(instruction_list)
file = 'Adv16Input.txt'
with open(file,'r') as f:
    instruction_list = f.read().split(',')

part_one = part_one_fn(instruction_list)
