from collections import deque

n, k = map(int, input().split())
tmp_lst = []
que = deque([i + 1 for i in range(n)])

while len(que) != 0:
    que.rotate(-k)
    tmp_lst.append(que.pop())

print('<' + ', '.join(map(str, tmp_lst)) + '>')