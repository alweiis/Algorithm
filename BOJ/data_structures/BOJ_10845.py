from sys import stdin
from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def size(self):
        return len(self.data)

    def empty(self):
        return int(len(self.data) == 0)

    def front(self):
        if not self.empty():
            return self.data[0]
        return -1

    def back(self):
        if not self.empty():
            return self.data[-1]
        return -1

    def pop(self):
        if not self.empty():
            return self.data.popleft()
        return -1

    def push(self, item):
        self.data.append(item)

Q = Queue()
n = int(stdin.readline().rstrip())
for _ in range(n):
    order = stdin.readline().rstrip()
    if order == 'pop':
        print(Q.pop())
    elif order == 'size':
        print(Q.size())
    elif order == 'empty':
        print(Q.empty())
    elif order == 'front':
        print(Q.front())
    elif order == 'back':
        print(Q.back())
    else:
        space_idx = order.rfind(' ')
        Q.push(int(order[space_idx + 1:]))