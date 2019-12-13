import numpy as np
from scipy.ndimage.measurements import label

##From Day 10
def rotate_left(l,n):
    ln = len(l)
    n %= ln
    a = l[n - ln:] + l[:n]
    return a

def rotate_right(l,n):
    ln = len(l)
    n %= ln
    a = l[-n:] + l[:-n]
    return a

def reverse(l,input_lengths,cur=0,skip=0):
    cur_list = l
    for i in input_lengths:
        #rotate so that always reversing first elements
        cur_list = rotate_left(cur_list,cur)
        rev = cur_list[:i]
        rev.reverse()
        cur_list[:i] = rev
        cur_list = rotate_right(cur_list,cur)
        cur += i + skip
        skip += 1
    return cur_list,cur,skip

def to_hex(i):
    hx = hex(i)
    hx = hx[-2:]
    if hx[0] == 'x':
        hx = '0' + hx[1]
    return hx

def ordify(input_lengths):
    instr = ''.join([str(i) for i in input_lengths])
    b = [ord(i) for i in instr]
    b += [17,31,73,47,23]
    return b

def knot_hash(input_string):
    l = list(range(256))
    input_lengths = ordify(input_string)
    cur = 0
    skip = 0
    for i in range(64):
        l,cur,skip = reverse(l,input_lengths,cur,skip)

    dense = []
    for i in range(16):
        xor = 0
        row = l[16*i:16*(i+1)]
        for j in row:
            xor ^= j
        dense.append(xor)
    hx = [to_hex(i) for i in dense]
    return ''.join(hx)

def part_one_fn(input_string):
    hex_rep = []
    for i in range(128):
        hex_rep.append(knot_hash(input_string + '-%i'%i))
    bin_rep = []
##    bin(int(h,16))[2:].zfill(4) for h in hex_rep
    for h in hex_rep:
        bin_rep_str = ''
        for char in h:
            bin_rep_str += bin(int(char,16))[2:].zfill(4)
        bin_rep.append([int(i) for i in list(bin_rep_str)])
    n = np.array(bin_rep)
    return n,n.sum()

p,part_one = part_one_fn('oundnydw')
#cheating with scipy
labeled_array, part_two = label(p)
