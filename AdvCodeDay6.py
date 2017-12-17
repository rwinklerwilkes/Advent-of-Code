import csv, math, itertools, copy, random
import numpy as np
from collections import Counter


##Day Six
def memory(memory_input):
    ctr = 0
    previous = set()
    matches = {}
    l = len(memory_input)
    bank = ','.join([str(i) for i in memory_input])
    while bank not in previous:
        matches[bank] = ctr
        previous.add(bank)
        max_ind = 0
        for i in range(l):
            if memory_input[i] > memory_input[max_ind]:
                max_ind = i
        remove_from = max_ind
        allocate = memory_input[remove_from]
        memory_input[remove_from] = 0
        cur_ind = (remove_from+1)%l
        while allocate > 0:
            memory_input[cur_ind] += 1
            allocate -= 1
            cur_ind += 1
            cur_ind %= l
        bank = ','.join([str(i) for i in memory_input])

        ctr += 1
    return ctr, ctr-matches[bank]

mi = [0,2,7,0]
memory_input = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
part_one, part_two = memory(memory_input)

