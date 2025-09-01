n = int(input())
lst = list(map(int, input().split()))
max_val = max(lst)
total = 0
for i in lst:
    total += (i / max_val) * 100

print(total / n)
