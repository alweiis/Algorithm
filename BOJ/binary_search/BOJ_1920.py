from sys import stdin
n = int(stdin.readline())
a_arr = sorted(map(int, stdin.readline().split()))
m = int(stdin.readline())
chk_arr = list(map(int, stdin.readline().split()))

def binary_search(arr, value):
    lower_idx = 0
    upper_idx = n - 1
    while lower_idx <= upper_idx:
        mid_idx = (lower_idx + upper_idx) // 2
        mid_value = arr[mid_idx]
        if value < mid_value:
            upper_idx = mid_idx - 1
        elif value > mid_value:
            lower_idx = mid_idx + 1
        elif value == mid_value:
            return 1
    return 0

for i in range(m):
    print(binary_search(a_arr, chk_arr[i]))