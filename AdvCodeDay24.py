class Node():
    def __init__(self,weight):
        self.weight = weight
        self.neighbors = []

    def add_neighbor(self,neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        return 'Weight: %i'%(self.weight)

def part_one_fn(input_list):
    all_nodes = {}
    for i in input_list:
        row = i.split('/')
        ndone = int(row[0])
        ndtwo = int(row[1])
        try:
            node_one = all_nodes[ndone]
        except:
            node_one = Node(ndone)
            all_nodes[ndone] = node_one
        try:
            node_two = all_nodes[ndtwo]
        except:
            node_two = Node(ndtwo)
            all_nodes[ndtwo] = node_two
        node_one.add_neighbor(node_two)
        node_two.add_neighbor(node_one)
    return all_nodes

input_list = ['0/2','2/2','2/3','3/4','3/5','0/1','10/1','9/10']
p = part_one_fn(input_list)
