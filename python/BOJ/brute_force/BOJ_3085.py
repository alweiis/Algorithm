n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

def swapy(x, y1, y2):
    arr[x][y1], arr[x][y2] = arr[x][y2], arr[x][y1]

def swapx(y, x1, x2):
    arr[x1][y], arr[x2][y] = arr[x2][y], arr[x1][y]

def check():
    global answer
    for i in range(n):
        cnt = 1
        for j in range(1, n):               # 행을 확인
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):               # 열을 확인
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

for i in range(n):
    for j in range(n):
        if j+1 < n and arr[i][j] != arr[i][j+1]:
            swapy(i, j, j+1)    # 행 고정, 열 변경
            check()
            swapy(i, j+1, j)    # 기존 상태로 복구

        if i+1 < n and arr[i][j] != arr[i+1][j]:
            swapx(j, i, i+1)    # 열 고정, 행 변경
            check()
            swapx(j, i+1, i)    # 기존 상태로 복구
print(answer)