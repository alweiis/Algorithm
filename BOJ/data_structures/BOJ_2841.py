from sys import stdin
input = stdin.readline
N, P = map(int, input().split())
stack = [[] for _ in range(7)]
count = 0
for _ in range(N):
    rn, pn = map(int, input().split())
    if stack[rn]:
        while stack[rn] and stack[rn][-1] > pn:
            stack[rn].pop()
            count += 1
        if stack[rn] and stack[rn][-1] == pn:
            continue
        stack[rn].append(pn)
        count += 1
    else:
        stack[rn].append(pn)
        count += 1
print(count)