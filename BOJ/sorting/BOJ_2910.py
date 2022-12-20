n, c = map(int, input().split())
arr = input().split()
answer = []
check = set()
for idx, val in enumerate(arr):
    if val not in check:
        check.add(val)
        cnt = arr.count(val)
        answer.append((cnt, idx, val))
answer.sort(key=lambda x: (-x[0], x[1]))
for x in answer:
    for _ in range(x[0]):
        print(x[2], end=' ')