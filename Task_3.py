class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]) if self.mins else val)

    def pop(self):
        self.mins.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.mins[-1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)

assert stack.get_min() == -3
stack.pop()
assert stack.top() == 0
assert stack.get_min() == -2
