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

def part_one_fn(instruction_list,l=None):
    if not l:
        l = [chr(i) for i in range(97,113)]
    for instruction in instruction_list:
        l = read_instruction(l,instruction)
##        print(''.join(l))
    return l

def find_cycle(instruction_list):
    #tortoise and hare algorithm
    ctr = 0
    slow = [chr(i) for i in range(97,113)]
    slow = part_one_fn(instruction_list,slow)
    fast = [chr(i) for i in range(97,113)]
    fast = part_one_fn(instruction_list,fast)
    fast = part_one_fn(instruction_list,fast)
    while ''.join(slow) != ''.join(fast):
        slow = part_one_fn(instruction_list,slow)
        fast = part_one_fn(instruction_list,fast)
        fast = part_one_fn(instruction_list,fast)
        ctr += 1

    return ctr
        

##instruction_list = ['s1','x3/4','pe/b']
##part_one_ex = part_one_ex_fn(instruction_list)
file = 'Adv16Input.txt'
with open(file,'r') as f:
    instruction_list = f.read().split(',')

part_one = ''.join(part_one_fn(instruction_list))
##part_two = part_two_fn(instruction_list)
m = find_cycle(instruction_list)
c = m+1
mod = 1000000000%c
p_two = part_one_fn(instruction_list)
for i in range(mod-1):
    p_two = part_one_fn(instruction_list,p_two)
part_two = ''.join(p_two)
