from sys import stdin
from collections import deque
class Queue:
    def __init__(self):
        self.data = deque()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.empty():
            return -1
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return int(self.size() == 0)

    def front(self):
        if self.empty():
            return -1
        return self.data[0]

    def back(self):
        if self.empty():
            return -1
        return self.data[-1]

Q = Queue()
n = int(stdin.readline())
for _ in range(n):
    command = stdin.readline().rstrip()
    if command == 'pop':
        print(Q.pop())
    elif command == 'size':
        print(Q.size())
    elif command == 'empty':
        print(Q.empty())
    elif command == 'front':
        print(Q.front())
    elif command == 'back':
        print(Q.back())
    else:
        command, num = command.split(' ')
        Q.push(int(num))