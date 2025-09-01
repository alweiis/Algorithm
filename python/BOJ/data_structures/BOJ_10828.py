from sys import stdin
class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def empty(self):
        return int(len(self.data) == 0)

    def top(self):
        if not self.empty():
            return self.data[-1]
        return -1

    def pop(self):
        if not self.empty():
            return self.data.pop()
        return -1

    def push(self, item):
        self.data.append(item)

S = Stack()
n = int(stdin.readline().rstrip())
for _ in range(n):
    order = stdin.readline().rstrip()
    if order == 'pop':
        print(S.pop())
    elif order == 'size':
        print(S.size())
    elif order == 'empty':
        print(S.empty())
    elif order == 'top':
        print(S.top())
    else:
        space_idx = order.rfind(' ')
        S.push(int(order[space_idx + 1:]))