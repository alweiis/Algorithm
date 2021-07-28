from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
v = int(stdin.readline())
print(nums.count(v))