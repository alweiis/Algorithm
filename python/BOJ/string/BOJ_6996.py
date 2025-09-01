t = int(input())
for _ in range(t):
    a, b = input().split()
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
        continue

    arr_a, arr_b = sorted(a), sorted(b)

    if arr_a == arr_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')