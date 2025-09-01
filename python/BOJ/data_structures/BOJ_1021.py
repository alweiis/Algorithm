from collections import deque
from itertools import islice
N, M = map(int, input().split())
order = list(map(int, input().split()))
cnt = 0
deq = deque([i for i in range(1, N+1)])
for num in order:
    if num == deq[0]:
        del deq[0]
    else:
        idx = deq.index(num)
        front_cnt, rear_cnt = len(list(islice(deq, idx))), len(list(islice(deq, idx+1, None)))
        if front_cnt > rear_cnt:
            while num != deq[0]:
                deq.rotate(1)
                cnt += 1
            del deq[0]
        else:
            while num != deq[0]:
                deq.rotate(-1)
                cnt += 1
            del deq[0]
print(cnt)