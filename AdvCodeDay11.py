import numpy as np
import math

directions = {'n':(0,1,-1),'ne':(1,0,-1),'nw':(-1,1,0),'s':(0,-1,1),'se':(1,-1,0),'sw':(-1,0,1)}
directions = {k:np.array(v) for k,v in directions.items()}

def cube_dist(a,b):
    return math.floor(sum(abs(a-b))/2)

def walk(in_string):
    in_list = [i for i in in_string.split(',')]
    start = np.zeros(3)
    position = np.zeros(3)
    max_dist = 0
    for i in in_list:
        position += directions[i]
        cur_dist = cube_dist(start,position)
        if cur_dist > max_dist:
            max_dist = cur_dist
    return cube_dist(start,position), max_dist

##in_string = 'se,sw,se,sw,sw'
file = 'AdvDay11Input.txt'
with open(file, 'r') as txtfile:
    in_string = txtfile.read()
part_one,part_two = walk(in_string)
