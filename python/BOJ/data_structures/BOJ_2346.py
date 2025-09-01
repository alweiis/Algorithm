from collections import deque
n = int(input())
balloon_nums = deque([i for i in range(1, n+1)])
balloon_orders = deque(map(int, input().split()))
result = []
while balloon_orders:
    rotation_cnt = balloon_orders.popleft()
    result.append(balloon_nums.popleft())
    if rotation_cnt > 0:
        balloon_orders.rotate(-(rotation_cnt - 1))
        balloon_nums.rotate(-(rotation_cnt - 1))
    else:
        balloon_orders.rotate(-rotation_cnt)
        balloon_nums.rotate(-rotation_cnt)
print(*result)