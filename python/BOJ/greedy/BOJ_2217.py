from sys import stdin
n = int(stdin.readline())
rope_arr = [int(stdin.readline()) for _ in range(n)]
rope_arr.sort(reverse=True)
max_weight = 0
for i in range(n):
    chk_weight = rope_arr[i] * (i+1)
    if chk_weight > max_weight:
        max_weight = chk_weight
print(max_weight)