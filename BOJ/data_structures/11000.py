import sys, heapq
input = sys.stdin.readline
n = int(input())
lecture = [tuple(map(int, input().split())) for _ in range(n)]
lecture.sort(key= lambda x: (x[0], x[1]))
heap = []
for start, end in lecture:
    if heap and heap[0] <= start:
            heapq.heappop(heap)
    heapq.heappush(heap, end)
print(len(heap))