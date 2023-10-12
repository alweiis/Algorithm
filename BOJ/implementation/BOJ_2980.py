from collections import deque
from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
light_check = {}
light_point = []
for _ in range(n):
    d, r, g = map(int, input().split())
    light_point.append(d)
    light_check[d] = deque([False] * r + [True] * g)
location, answer = 0, 0

while location < l:
    if location not in light_point:
        location += 1
        answer += 1
        for i in light_point:
            light_check[i].rotate(-1)
    else:
        while not light_check[location].index(0):
            answer += 1
            for i in light_point:
                light_check[i].rotate(-1)
        else:
            location += 1
            answer += 1
            for i in light_point:
                light_check[i].rotate(-1)
print(answer)