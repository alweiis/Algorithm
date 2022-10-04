m, n = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
answer = sorted(a - b)
if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)