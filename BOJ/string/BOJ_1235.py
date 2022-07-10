import sys
input = sys.stdin.readline

N = int(input())
numbers = [input().rstrip() for _ in range(N)]
k = 1
while True:
    check = set()
    for number in numbers:
        check.add(number[-k:])
    if len(check) == N:
        break
    k += 1
print(k)