n, b = map(int, input().split())
answer = ''
while n > 0:
    n, r = divmod(n, b)
    if 10 <= r <= 35:
        r = chr(r + 55)
    else:
        r = str(r)
    answer += r
print(answer[::-1])