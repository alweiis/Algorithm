from sys import stdin
n, k = map(int, stdin.readline().split())
numbers = sorted(map(int, stdin.readline().split()))
print(numbers[k - 1])