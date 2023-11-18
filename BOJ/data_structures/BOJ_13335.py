from collections import deque
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque([0] * w)
time, idx = 0, 0
while idx < n:
    bridge.popleft()
    if sum(bridge) + trucks[idx] <= l:
        bridge.append(trucks[idx])
        idx += 1
    else:
        bridge.append(0)
    time += 1
time += len(bridge)
print(time)