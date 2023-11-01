from sys import stdin
input = stdin.readline

n, k, b = map(int, input().split())
available = [1] * n
for _ in range(b):
    idx = int(input())
    available[idx-1] = 0
prefix_sum = sum(available[:k])
answer = [prefix_sum]
for i in range(n-k):
    prefix_sum += available[i+k] - available[i]
    answer.append(prefix_sum)
answer.sort(reverse=True)
print(k-answer[0])