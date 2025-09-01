from sys import stdin
arr = [i for i in range(20 + 1)]
for _ in range(10):
    a, b = map(int, stdin.readline().split())
    tmp_arr = arr[:a] + arr[a:b + 1][::-1] + arr[b + 1:]
    arr = tmp_arr
print(' '.join(map(str, arr[1:])))