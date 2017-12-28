class StateMachine():
    def __init__(self):
        self.ptr = 0
        self.ones = set()
        self.state = 'A'

    def move(self):
        one = False
        next_state = self.state
        if self.ptr in self.ones:
            one = True
        if self.state == 'A':
            if one:
                self.ones.remove(self.ptr)
                self.ptr -= 1
                next_state = 'F'
            else:
                self.ones.add(self.ptr)
                self.ptr += 1
                next_state = 'B'
        elif self.state == 'B':
            if one:
                self.ones.remove(self.ptr)
                self.ptr += 1
                next_state = 'D'
            else:
                self.ptr += 1
                next_state = 'C'
        elif self.state == 'C':
            if one:
                self.ptr += 1
                next_state = 'E'
            else:
                self.ones.add(self.ptr)
                self.ptr -= 1
                next_state = 'D'
        elif self.state == 'D':
            if one:
                self.ones.remove(self.ptr)
                self.ptr -= 1
            else:
                self.ptr -= 1
                next_state = 'E'
        elif self.state == 'E':
            if one:
                self.ptr += 1
                next_state = 'C'
            else:
                self.ptr += 1
                next_state = 'A'
        elif self.state == 'F':
            if one:
                self.ptr += 1
                next_state = 'A'
            else:
                self.ones.add(self.ptr)
                self.ptr -= 1
                next_state = 'A'
        return next_state

    def part_one_fn(self):
        for i in range(12794428):
            self.state = self.move()
        return len(self.ones)

s = StateMachine()
