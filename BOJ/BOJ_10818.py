n = int(input())
lst = input().split()
max_val, min_val = int(lst[0]), int(lst[0])

for i in range(1, n):
    chk_val = int(lst[i])
    if max_val < chk_val:
        max_val = chk_val
    if min_val > chk_val:
        min_val = chk_val

print(min_val, max_val)
