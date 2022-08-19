from collections import deque
a, b = map(int, input().split())

answer = -1
def bfs(start):
    global answer
    q = deque([(start, 1)])
    while q:
        curr_num, count = q.popleft()
        if curr_num == b:
            answer = count
            break
        for next_num in [(curr_num * 10) + 1, curr_num * 2]:
            if next_num <= b:
                q.append((next_num, count + 1))

bfs(a)
print(answer)