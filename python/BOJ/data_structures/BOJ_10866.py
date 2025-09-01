from sys import stdin
from collections import deque

class Deque:
    def __init__(self):
        self.data = deque()

    def push_front(self, item):
        self.data.appendleft(item)

    def push_back(self, item):
        self.data.append(item)

    def size(self):
        return len(self.data)

    def empty(self):
        return int(len(self.data) == 0)

    def pop_front(self):
        if self.empty():
            return -1
        return self.data.popleft()

    def pop_back(self):
        if self.empty():
            return -1
        return self.data.pop()

    def front(self):
        if self.empty():
            return -1
        return self.data[0]

    def back(self):
        if self.empty():
            return -1
        return self.data[-1]

D = Deque()
n = int(stdin.readline())
for _ in range(n):
    order = stdin.readline().split()
    if order[0] == 'push_front':
        D.push_front(order[1])
    elif order[0] == 'push_back':
        D.push_back(order[1])
    elif order[0] == 'pop_front':
        print(D.pop_front())
    elif order[0] == 'pop_back':
        print(D.pop_back())
    elif order[0] == 'size':
        print(D.size())
    elif order[0] == 'empty':
        print(D.empty())
    elif order[0] == 'front':
        print(D.front())
    elif order[0] == 'back':
        print(D.back())