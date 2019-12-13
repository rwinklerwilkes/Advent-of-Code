all_nodes = {}

class Node():
    def __init__(self,label):
        self.label = label
        self.visited = False
        self.group = None
        self.neighbors = []

    def add_neighbor(self,neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        return 'Node: %i'%self.label

def part_one_fn():
    start_node = all_nodes[0]
    stack = [start_node]
    ctr = 0
    while stack:
        cur_node = stack.pop()
        if not cur_node.visited:
            cur_node.visited = True
            stack += cur_node.neighbors
            ctr += 1
    return ctr

def part_two_fn():
    #reset all visited flags
    for k,v in all_nodes.items():
        v.visited = False
    
    group_to_use = 0
    for k in all_nodes.keys():
        cur_node = all_nodes[k]
        if cur_node.group is None:
            stack = [cur_node]
            while stack:
                cur_node = stack.pop()
                if not cur_node.visited:
                    cur_node.visited = True
                    stack += cur_node.neighbors
                    cur_node.group = group_to_use
            group_to_use += 1
    return group_to_use
    

file = 'AdvDay12Input.txt'
with open(file, 'r') as txtfile:
    for row in txtfile:
##input_text = ['0 <-> 2','1 <-> 1','2 <-> 0, 3, 4','3 <-> 2, 4','4 <-> 2, 3, 6','5 <-> 6','6 <-> 4, 5']
##for row in input_text:
        split_row = row.split()
        label = int(split_row[0])
        try:
            n = all_nodes[label]
        except:
            n = Node(label)
            all_nodes[label] = n
        neighbor_set = split_row[2:]
        neighbor_set = [int(n.replace(',','')) for n in neighbor_set]
        for label in neighbor_set:
            try:
                neighbor = all_nodes[label]
            except:
                neighbor = Node(label)
                all_nodes[label] = neighbor
            n.add_neighbor(neighbor)
            neighbor.add_neighbor(n)

part_one = part_one_fn()
part_two = part_two_fn()
