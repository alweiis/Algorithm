n = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = list(map(int, input().split()))
s = 0
for i in range(n):
    min_num = min(b)
    b.remove(min_num)
    s += a[i] * min_num
print(s)