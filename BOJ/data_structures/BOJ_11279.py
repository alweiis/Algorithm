from sys import stdin
import heapq

heap = []

n = int(stdin.readline())
for _ in range(n):
    x = int(stdin.readline())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))