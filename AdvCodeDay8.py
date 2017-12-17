def check_condition(registers,condition):
    check_r = condition[0]
    check_for = condition[1]
    check_val = int(condition[2])
    ret_val = None
    if check_for == '>':
        ret_val = registers[check_r] > check_val
    elif check_for == '>=':
        ret_val = registers[check_r] >= check_val
    elif check_for == '<':
        ret_val = registers[check_r] < check_val
    elif check_for == '<=':
        ret_val = registers[check_r] <= check_val
    elif check_for == '==':
        ret_val = registers[check_r] == check_val
    elif check_for == '!=':
        ret_val = registers[check_r] != check_val
    return ret_val

def process_instructions(instruction_list):
    registers = {}
    max_val = 0
    for in_string in instruction_list:
        s = in_string.split()
        register = s[0]
        inc_dec = s[1]
        amt = int(s[2])
        condition = s[4:]
        if register not in registers:
            registers[register] = 0
        if condition[0] not in registers:
            registers[condition[0]] = 0
        condition_met = check_condition(registers,condition)
        if condition_met:
            val = registers[register]
            if inc_dec == 'inc':
                val += amt
            else:
                val -= amt
            registers[register] = val
            if val > max_val:
                max_val = val
    return max(registers.values()), max_val


##ins = ['b inc 5 if a > 1','a inc 1 if b < 5','c dec -10 if a >= 1','c inc -20 if c == 10']
instructions = []
file = 'Adv8Input.txt'
with open(file,'r') as f:
    for row in f:
        instructions.append(row.strip())
part_one, part_two = process_instructions(instructions)
