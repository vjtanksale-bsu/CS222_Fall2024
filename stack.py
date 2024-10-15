class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("Can't pop from empty stack")
    def isEmpty(self):
        return len(self.items) == 0