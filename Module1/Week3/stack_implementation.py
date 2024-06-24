class MyStack:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.stack = []

    def is_empty(self):

        return len(self.stack) == 0

    def is_full(self):

        return len(self.stack) == self.capacity

    def pop(self):

        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, value):

        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack.append(value)

    def top(self):

        if self.is_empty():
            return None
        return self.stack[-1]
