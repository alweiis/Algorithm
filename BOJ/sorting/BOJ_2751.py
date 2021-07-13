from sys import stdin
n = int(input())
num_lst = [int(stdin.readline().rstrip()) for _ in range(n)]
num_lst.sort()
for number in num_lst:
    print(number)