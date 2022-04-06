n = int(input())
p = sorted(map(int, input().split()))
time = 0
for i in range(n):
    time += sum(p[:i+1])
print(time)