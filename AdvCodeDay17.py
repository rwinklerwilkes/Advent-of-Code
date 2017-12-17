from collections import deque

def part_one_fn(step_size):
    new_list = [0]
    cur_pos = 0
    for i in range(1,2018):
        new_pos = (cur_pos+step_size)%len(new_list)
        #insert after, not before
        new_pos += 1
        new_list.insert(new_pos,i)
        cur_pos = new_pos
##        print(new_list)
    return new_list[cur_pos+1]

def part_one_fn_deque(step_size):
    new_list = deque([0])
    for i in range(1,2018):
        new_list.rotate(-step_size)
        new_list.append(i)
    ind = new_list.index(2017)
    return new_list[0]

def part_two_fn(step_size):
    new_list = [0]
    cur_pos = 0
    for i in range(1,50000001):
        new_pos = (cur_pos+step_size)%len(new_list)
        #insert after, not before
        new_pos += 1
        new_list.insert(new_pos,i)
        cur_pos = new_pos
##        print(new_list)
    ind = new_list.index(0)
    return new_list[ind+1]

def part_two_fn_deque(step_size):
    new_list = deque([0])
    for i in range(1,50000001):
        new_list.rotate(-step_size)
        new_list.append(i)
    ind = new_list.index(0)
    return new_list[ind+1]

part_one = part_one_fn(356)
##part_two = part_two_fn(356)
part_two = part_two_fn_deque(356)
