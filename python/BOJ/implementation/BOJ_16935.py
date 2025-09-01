from sys import stdin
input = stdin.readline

def rotate_arr(arr, n, m, r):
    answer = []
    if r == 1:
        for i in range(n-1, -1, -1):
            answer.append(arr[i])
    elif r == 2:
        for i in range(n):
            answer.append(list(reversed(arr[i])))
    elif r == 3:
        for j in range(m):
            temp = []
            for i in range(n-1, -1, -1):
                temp.append(arr[i][j])
            answer.append(temp)
    elif r == 4:
        for j in range(m-1, -1, -1):
            temp = []
            for i in range(n):
                temp.append(arr[i][j])
            answer.append(temp)
    elif r == 5:
        check = []
        for i in range(n//2, n):
            temp1, temp2 = [], []
            for j in range(m//2):
                temp1.append(array[i][j])
            for j in range(m//2, m):
                temp2.append(array[i][j])
            answer.append(temp1)
            check.append(temp2)
        for i in range(n//2):
            temp1, temp2 = [], []
            for j in range(m//2):
                temp1.append(array[i][j])
            for j in range(m//2, m):
                temp2.append(array[i][j])
            answer[i].extend(temp1)
            check[i].extend(temp2)
        answer.extend(check)
    elif r == 6:
        check = []
        for i in range(n // 2):
            temp1, temp2 = [], []
            for j in range(m // 2, m):
                temp1.append(array[i][j])
            for j in range(m // 2):
                temp2.append(array[i][j])
            answer.append(temp1)
            check.append(temp2)
        for i in range(n // 2, n):
            temp1, temp2 = [], []
            for j in range(m // 2, m):
                temp1.append(array[i][j])
            for j in range(m // 2):
                temp2.append(array[i][j])
            answer[i-(n//2)].extend(temp1)
            check[i-(n//2)].extend(temp2)
        answer.extend(check)
    return answer

N, M, _ = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))
for R in operations:
    array = rotate_arr(array, len(array), len(array[0]), R)
for arr in array:
    print(*arr)