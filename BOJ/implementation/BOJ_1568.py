n = int(input())
second = 0
cnt = 1
while n:
    if n - cnt >= 0:
        n -= cnt
        second += 1
        cnt += 1
    else:
        cnt = 1
print(second)