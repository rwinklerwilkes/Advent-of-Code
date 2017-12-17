from collections import Counter

##Day Seven
all_nodes = {}

class Node():
    def __init__(self,name,weight,children=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None

    def add_children(self):
        if self.children:
            self.children = [all_nodes[c] for c in self.children]
            for child in self.children:
                child.parent = self

    def calculate_weight(self):
        sm = 0
        try:
            for child in self.children:
                sm += child.calculate_weight()
        except:
            pass
        sm += self.weight
        self.tower_weight = sm
        return self.tower_weight

    def __repr__(self):
        return self.name + ' Weight %i Tower Weight %i'%(self.weight,self.tower_weight)

def find_root(node):
    p = node
    while p.parent is not None:
        p = p.parent
    return p

def dfs(node):
    stack = [node]
    while stack:
        cur_node = stack.pop()
        if cur_node.children:
            stack += cur_node.children

def find_bad_node(root):
    stack = [root]
    while stack:
        cur_node = stack.pop()
        #are all children balanced?
        if cur_node.children:
            weights = [c.tower_weight for c in cur_node.children]
            if max(weights) == min(weights):
                #keep going
                stack += cur_node.children
            else:
                #found an issue - is it with root or one of children?
                ctr = {v:k for k,v in Counter(weights).items()}
                bad_weight = ctr[1]
                weight_diff = ctr[max(ctr.keys())] - ctr[1]
                for child in cur_node.children:
                    if child.tower_weight == bad_weight:
                        bad_node = child
                weights = [c.tower_weight for c in bad_node.children]
                #children are balanced
                if max(weights) == min(weights):
                    return bad_node.weight + weight_diff
                #children aren't balanced - push bad node
                else:
                    stack.append(bad_node)

##file = "Tower Input Sm.txt"
file = "Tower Input.txt"

with open(file, 'r') as txtfile:
    for row in txtfile:
        s = row.strip().split()
        #No children
        name = s[0]
        weight = int(s[1][1:-1])
        if len(s) == 2:
            n = Node(name,weight)
        #Has children
        else:
            children = s[3:]
            children = [c.replace(',','') for c in children]
            n = Node(name,weight,children)
        all_nodes[name] = n

for n in all_nodes.values():
    n.add_children()

part_one = find_root(n)
part_one.calculate_weight()
part_two = find_bad_node(part_one)
