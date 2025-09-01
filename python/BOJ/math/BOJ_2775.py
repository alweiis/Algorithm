arr = [[1] * 15 for _ in range(15)]
arr[14] = [i for i in range(1, 15)]
for i in range(13, -1, -1):
    for j in range(1, 15):
        arr[i][j] = sum(arr[i+1][:j+1])

T = int(input())
for _ in range(T):
    k = int(input())    # 층
    n = int(input())    # 호
    print(arr[14-k][n-1])