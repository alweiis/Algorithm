N = int(input())
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []
answer = abs(N - 100)
for i in range(1000000 + 1):
    for j in str(i):
        if int(j) in broken:
            break
    else:
        answer = min(answer, abs(N - i) + len(str(i)))
print(answer)