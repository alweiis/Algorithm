from heapq import heappush, heappop
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []
for card in cards:
    heappush(heap, card)
while m:
    x = heappop(heap)
    y = heappop(heap)
    heappush(heap, x + y)
    heappush(heap, x + y)
    m -= 1
print(sum(heap))