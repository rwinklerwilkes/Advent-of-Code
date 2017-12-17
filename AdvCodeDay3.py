import math, itertools
import numpy as np

##Day Three
def mandist(square):
    psq = math.floor(math.sqrt(square))
    if psq%2==0:
        psq -= 1
    nsq = math.ceil(math.sqrt(square))
    if nsq%2==0:
        nsq += 1
    direct = [(0,1),(-1,0),(0,-1),(1,0)]
    direct = [np.array(i) for i in direct]
    nsq_coord = (nsq-1)/2
    max_pos = np.array((nsq_coord,nsq_coord))
    cur_pos = np.array((nsq_coord,-(nsq_coord-1)))
    cur_num = psq**2 + 1
    for d in direct:
        while all(abs((d * (cur_pos + d))) <= (nsq_coord,nsq_coord)) and cur_num < square:
            cur_pos += d
            cur_num += 1
    return sum(abs(cur_pos))

def mandist_large(square):
    prev = {(0,0):(1,0)}
    ctr = 1
    largest = 1
    cur_pos = np.array((1,0))
    neighbors = [np.array(i) for i in itertools.product([-1,0,1],repeat=2)]
    direct = [(0,1),(-1,0),(0,-1),(1,0)]
    direct = [np.array(i) for i in direct]
    nsq_coord = 1
    while True:
        for d in direct:
            while all(abs((d * (cur_pos + d))) <= (nsq_coord,nsq_coord)) or all(cur_pos == np.array((nsq_coord,-nsq_coord))):
##                print(cur_pos)
                n_set = [n + cur_pos for n in neighbors]
                n_set = [tuple(n) for n in n_set]
                new_sum = 0
                for neighbor in n_set:
                    try:
                        cur_neighbor = prev[neighbor]
                        if cur_neighbor[1] < ctr:
                            new_sum += cur_neighbor[0]
                    except:
                        pass
                largest = new_sum
                if largest > square:
                    return largest
                prev[tuple(cur_pos)] = (new_sum,ctr)
                cur_pos += d
                ctr += 1
##        cur_pos += (1,0)
        nsq_coord += 1
    return prev
    

part_one = mandist(325489)
part_two = mandist_large(325489)
