import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    answer = max_stock = 0
    for i in range(n-1, -1, -1):
        if stock[i] > max_stock:
            max_stock = stock[i]
        else:
            answer += max_stock - stock[i]
    print(answer)