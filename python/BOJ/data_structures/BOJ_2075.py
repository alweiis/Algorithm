import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    for num in map(int, input().split()):
        if len(heap) >= n:
            heapq.heappushpop(heap, num)
        else:
            heapq.heappush(heap, num)
print(heapq.heappop(heap))