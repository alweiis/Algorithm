from  collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    key1 = input().split()
    key2 = input().split()
    password = input().split()
    answer = ['-'] * n
    check = defaultdict(list)
    for idx, key in enumerate(key1):
        check[key].append(idx)
    for idx, key in enumerate(key2):
        check[key].append(idx)
    for start, end in check.values():
        answer[start] = password[end]
    print(' '.join(answer))