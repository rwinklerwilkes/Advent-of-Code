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

def part_two_fn(input_lengths):
    l = list(range(256))
    input_lengths = ordify(input_lengths)
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

##a = list(range(5))
##input_lengths = [3,4,1,5]


input_lengths = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
a = list(range(256))
a = reverse(a,input_lengths)
part_one = a[0]*a[1]

input_lengths = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
part_two = part_two_fn(input_lengths)
