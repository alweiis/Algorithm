a, b = input().split()
answer = len(a)
for i in range(len(b) - len(a) + 1):
    tmp = b[i:i+len(a)]
    count = 0
    for j in range(len(a)):
        if a[j] != tmp[j]:
            count += 1
    answer = min(answer, count)
print(answer)