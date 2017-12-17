start_a = 679
start_b = 771
##start_a = 65
##start_b = 8921
gen_a = 16807
gen_b = 48271
mod_val = 2147483647

def a_gen():
    x = start_a
    while True:
        x *= gen_a
        x %= mod_val
        if x%4==0:
            yield x

def b_gen():
    x = start_b
    while True:
        x *= gen_b
        x %= mod_val
        if x%8==0:
            yield x

def part_one_fn(start_a,start_b):
    total = 0
    A = a_gen()
    B = b_gen()
    for i in range(5000000):
        a_val = next(A)
        b_val = next(B)
        if a_val & 0xFFFF == b_val&0xFFFF:
            total += 1
        prev_a, prev_b = a_val,b_val
    return total

part_one = part_one_fn(start_a,start_b)
