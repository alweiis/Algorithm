import sys
input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 1000001
arr = [0] * MAX
for _ in range(n):
    g, x = map(int, input().split())
    arr[x-1] = g
section = 2 * k + 1
window = sum(arr[:section])
answer = window
for i in range(section, MAX):
    window += arr[i] - arr[i - section]
    answer = max(answer, window)
print(answer)