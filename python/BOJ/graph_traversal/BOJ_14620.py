def bfs(x, y):
    answer = []

    return min(answer)


n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
price = float('inf')
for i in range(1, n - 2):
    for j in range(1, n - 2):
        result = bfs(i, j)
        price = min(price, result)
print(price)