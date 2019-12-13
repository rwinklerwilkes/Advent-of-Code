import math
import numpy as np

facing = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
facing = {k:np.array(v) for k,v in facing.items()}
cd = ['u','r','d','l']

##Part One
def print_map(infected,pos):
    l = np.full((8,8),'.')
    for i in infected:
        n = np.array(i) + np.array((4,4))
        l[tuple(n)] = '#'
    p = pos + np.array((4,4))
    l[tuple(p)] = '[' + l[tuple(p)] + ']'
##    print(l)

def move(pos,face_dir,infected):
    cur_ind = cd.index(face_dir)
    ret_val = 0
    if tuple(pos) in infected:
        infected.remove(tuple(pos))
        cur_ind += 1
    else:
        infected.add(tuple(pos))
        cur_ind -= 1
        ret_val += 1
    cur_ind %= len(cd)
    new_dir = cd[cur_ind]
    pos += facing[new_dir]
    return pos,new_dir,infected,ret_val

def part_one_fn(start_map,iterations):
    infected = set()
    start_map = [list(row) for row in start_map]
    for i in range(len(start_map)):
        for j in range(len(start_map[i])):
            if start_map[i][j] == '#':
                infected.add((i,j))
    start_ind = math.floor(len(start_map)/2)
    pos = np.array((start_ind,start_ind))
    face_dir = 'u'
    ctr = 0
##    print_map(infected,pos)
    for i in range(iterations):
        pos, face_dir,infected,ret_val = move(pos,face_dir,infected)
##        print_map(infected,pos)
        ctr += ret_val
    return ctr

##Part Two
def print_map_2(infected,pos):
    l = np.full((8,8),'.')
    for k,v in infected.items():
        n = np.array(k) + np.array((4,4))
        l[tuple(n)] = v
    p = pos + np.array((4,4))
    l[tuple(p)] = '[' + l[tuple(p)] + ']'
    print(l)

def move_2(pos,face_dir,infected):
    cur_ind = cd.index(face_dir)
    ret_val = 0
    #Decide what to do at current position
    try:
        cur_pos_val = infected[tuple(pos)]
    except:
        cur_pos_val = '.'
    if cur_pos_val == '.':
        #becomes weakened
        infected[tuple(pos)] = 'W'
        cur_ind -= 1
    elif cur_pos_val == 'W':
        #becomes infected
        infected[tuple(pos)] = '#'
        ret_val += 1
    elif cur_pos_val == '#':
        #becomes flagged
        infected[tuple(pos)] = 'F'
        cur_ind += 1
    else:
        #becomes clean
        infected.pop(tuple(pos),None)
        #reverses direction
        cur_ind += 2
        
    cur_ind %= len(cd)
    new_dir = cd[cur_ind]
    pos += facing[new_dir]
    return pos,new_dir,infected,ret_val

def part_two_fn(start_map,iterations):
    infected = {}
    start_map = [list(row) for row in start_map]
    for i in range(len(start_map)):
        for j in range(len(start_map[i])):
            if start_map[i][j] == '#':
                infected[(i,j)] = '#'
    start_ind = math.floor(len(start_map)/2)
    pos = np.array((start_ind,start_ind))
    face_dir = 'u'
    ctr = 0
##    print_map_2(infected,pos)
    for i in range(iterations):
        pos, face_dir,infected,ret_val = move_2(pos,face_dir,infected)
##        print_map_2(infected,pos)
        ctr += ret_val
    return ctr
        
##start_map = ['..#','#..','...']
start_map = []
file = 'Adv22Input.txt'
with open(file,'r') as f:
    for row in f.readlines():
        start_map.append(row.strip())
part_one = part_one_fn(start_map,10000)
part_two = part_two_fn(start_map,10000000)
