from sys import stdin
input = stdin.readline

n = int(input())
max_h, max_idx = 0, 0
pillar = [0] * 1001
answer = 0
for _ in range(n):
    l, h = map(int, input().split())
    pillar[l] = h
    if max_h < h:
        max_h, max_idx = h, l
curr_pillar = 0
for i in range(max_idx+1):
    curr_pillar = max(curr_pillar, pillar[i])
    answer += curr_pillar
curr_pillar = 0
for i in range(1000, max_idx, -1):
    curr_pillar = max(curr_pillar, pillar[i])
    answer += curr_pillar
print(answer)