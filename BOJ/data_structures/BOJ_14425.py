from sys import stdin
n, m = map(int, stdin.readline().split())
s = {stdin.readline().rstrip() for _ in range(n)}
count = 0
for _ in range(m):
    chk_str = stdin.readline().rstrip()
    if chk_str in s:
        count += 1
print(count)