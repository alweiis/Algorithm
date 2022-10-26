def solution(n, arr1, arr2):
    arr1 = find_password(arr1)
    arr2 = find_password(arr2)
    answer = [''] * n
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer[i] = tmp
    return answer

def find_password(arr):
    for i in range(len(arr)):
        tmp = format(arr[i], 'b')
        while len(tmp) < len(arr):
            tmp = '0' + tmp
        arr[i] = tmp
    return arr