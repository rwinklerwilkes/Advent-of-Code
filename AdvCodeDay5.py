import copy

##Day Five
def jump(jump_input):
    ctr = 0
    start_ind = 0
    while start_ind >= 0 and start_ind < len(jump_input):
        next_ind = start_ind + jump_input[start_ind]
        jump_input[start_ind] += 1
        start_ind = next_ind
        ctr += 1
    return ctr

def jump_two(jump_input):
    ctr = 0
    start_ind = 0
    while start_ind >= 0 and start_ind < len(jump_input):
        next_ind = start_ind + jump_input[start_ind]
        if jump_input[start_ind] >= 3:
            jump_input[start_ind] -= 1
        else:
            jump_input[start_ind] += 1
        start_ind = next_ind
        ctr += 1
    return ctr

file = "Jump Input.txt"
jump_instructions = []

ji = [0,3,0,1,-3]
with open(file, 'r') as txtfile:
    for row in txtfile:
        jump_instructions.append(int(row.strip()))
jump_instructions_cpy = copy.deepcopy(jump_instructions)

part_one = jump(jump_instructions)
part_two = jump_two(jump_instructions_cpy)
