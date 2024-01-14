from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
stack = []
deq = deque()
for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        if command[0] == '1':
            deq.append(command[1])
        else:
            deq.appendleft(command[1])
        stack.append(command[0])
    else:
        if stack:
            num = stack.pop()
            if num == '1':
                deq.pop()
            else:
                deq.popleft()
print(''.join(deq) if len(deq) else 0)