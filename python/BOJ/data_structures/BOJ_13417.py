from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    deq = deque(arr[0])
    for i in range(1, len(arr)):
        if arr[i] <= deq[0]:
            deq.appendleft(arr[i])
        else:
            deq.append(arr[i])
    print(''.join(deq))