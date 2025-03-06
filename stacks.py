class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            return "Stack Overflow"
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Empty stack"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return print("Empty Stack")

    def is_empty(self):
        return self.stack == []


    def print_stack(self):
        return print(self.stack)

    def __str__(self):
        return "".join(str(i) for i in self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack)
# print(stack.pop())
# stack.print_stack()
stack.is_empty()