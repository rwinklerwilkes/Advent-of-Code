class Stack():
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

def read_stream(string):
    s = Stack()
    in_garbage = False
    canceled = False
    grp = 1
    ret_sum = 0
    ct = 0
    for char in string:
##        print('%s in_garbage = %s, canceled = %s'%(char,in_garbage,canceled))
        if canceled:
            canceled = False
            continue
        if char == '{' and not in_garbage:
            s.push(('{',grp))
            grp += 1
        elif char == '}' and not in_garbage:
            grp = s.pop()[1]
            ret_sum += grp
        elif char == '<' and not in_garbage:
            in_garbage = True
            s.push(('<',0))
            ct -= 1
        elif char == '>' and in_garbage:
##            #are we ignoring characters or not?
##            if canceled:
##                pass
##            else:
            s.pop()
            in_garbage = False
        if char == '!':
            canceled = True
            continue
        if in_garbage:
            ct += 1
    return ret_sum, ct

test_string = '<random characters>'
test_string = '<{o"i!a,<{i<a>'
file = 'Adv9Input.txt'
input_string = None
with open(file,'r') as f:
    input_string = f.read()
r,ct = read_stream(input_string)
