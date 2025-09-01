n, k = map(int, input().split())
temperature = list(map(int, input().split()))
temp = sum(temperature[:k])
answer = temp
for i in range(k, n):
    temp += temperature[i] - temperature[i-k]
    answer = max(answer, temp)
print(answer)
