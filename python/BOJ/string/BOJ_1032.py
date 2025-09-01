n = int(input())
arr = [input() for _ in range(n)]
pattern = ''
for i in range(len(arr[0])):
    tmp = arr[0][i]
    for j in range(1, n):
        if arr[j][i] != tmp:
            tmp = '?'
    pattern += tmp
print(pattern)