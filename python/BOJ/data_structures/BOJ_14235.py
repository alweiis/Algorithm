import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    presents = list(map(int, input().split()))
    if presents[0] == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(-1)
    else:
        for i in range(1, len(presents)):
            heapq.heappush(heap, (-presents[i], presents[i]))