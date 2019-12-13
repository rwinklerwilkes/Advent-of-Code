class Layer():
    def __init__(self,label,move_range):
        self.label = label
        self.move_range = move_range
        self.cur_pos = 0
        self.ud = -1

    def move(self):
        if self.cur_pos == 0 or self.cur_pos == self.move_range - 1:
            self.ud = -self.ud

        self.cur_pos += self.ud

    def __repr__(self):
        return 'Layer %i Range %i Position %i'%(self.label,self.move_range,self.cur_pos)

    def at_top(self,time):
        return time%((self.move_range-1)*2)==0

def part_one_fn(layers):
    m = max(layers.keys())
    cur_pos = -1
    ret_sum = 0
    while cur_pos <= m:
        cur_pos += 1
        try:
            cur_l = layers[cur_pos]
            if cur_l.cur_pos == 0:
                ret_sum += cur_l.label * cur_l.move_range
        except:
            pass
        for layer in layers.values():
            layer.move()
    return ret_sum

##def part_two_fn(layers):
##    delay = 0
##    m = max(layers.keys())
##    passed = False
##    while not passed:
##        check_all = [i+delay for i in range(m+1)]
##        at_top = [False for c in check_all]
##        for i in range(len(at_top)):
##            try:
##                at_top[i] = layers[i].at_top(check_all[i])
##            except:
##                at_top[i] = False
##        if not any(at_top):
##            passed = True
##            break
##        delay += 1
##    return delay

def part_two_fn(layers):
    m = max(layers.keys())
    l = [0 for i in range(m+1)]
    for i in range(len(l)):
        try:
            l[i] = layers[i].move_range
        except:
            l[i] = 1

    delay = 0
    passed = False
    while not passed:
##        if delay % 1000 == 0:
##            print(delay)
        d = [(i+delay)%((l[i]-1)*2) if l[i]!=1 else 1 for i in range(len(l))]
        check = [i!=0 for i in d]
        if all(check):
            passed = True
            break
        delay += 1
    return delay

##inlist = ['0: 3','1: 2','4: 4','6: 4']
inlist = []
file = 'Adv13Input.txt'
with open(file,'r') as f:
    for row in f:
        inlist.append(row)
layers = {}
for row in inlist:
    r = row.split(':')
    label = int(r[0])
    mr = int(r[1].strip())
    layers[label] = Layer(label,mr)

##part_one = part_one_fn(layers)
part_two = part_two_fn(layers)
