from collections import deque

n = int(input())
snow = deque(sorted(map(int, input().split()), reverse=True))
time = 0
while len(snow) >= 2:
    a = snow.popleft() - 1
    b = snow.popleft() - 1
    if b > 0:
        snow.appendleft(b)
    if a > 0:
        snow.appendleft(a)
    time += 1
    snow = deque(sorted(snow, reverse=True))
if len(snow) == 1:
    time += snow[0]
print(-1 if time > 1440 else time)