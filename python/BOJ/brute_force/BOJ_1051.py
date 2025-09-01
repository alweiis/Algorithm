n, m = map(int, input().split())
rectangle = [list(map(int, input())) for _ in range(n)]
area = 1
k = min(n, m)
l = 1
while l < k:
    for i in range(n):
        for j in range(len(rectangle[i])):
            if 0 <= i+l < n and 0 <= j+l < m:
                if rectangle[i][j] == rectangle[i][j+l] == rectangle[i+l][j] == rectangle[i+l][j+l]:
                    area = max(area, (l+1) ** 2)
    l += 1
print(area)