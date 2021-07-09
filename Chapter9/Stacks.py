class Stack:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        if len(self.s) != 0:
            return self.s.pop()
        return None

    def __repr__(self) -> str:
        return f'Stack: {self.s}'


if __name__ == '__main__':
    stack = Stack()
    for _ in range(5):
        stack.push(_)

    print(stack)
    
    for _ in range (5):
        stack.pop()

    print("Stack after removal")
    print(stack)