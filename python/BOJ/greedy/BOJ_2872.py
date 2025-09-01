from sys import stdin
input = stdin.readline

n = int(input())
books = dict()
for i in range(1, n+1):
    number = int(input())
    books[number] = i
sort_cnt = 0
small_num = n - 1
large_num = n
while small_num > 0:
    small_num_idx = books[small_num]
    large_num_idx = books[large_num]
    if small_num_idx > large_num_idx:
        books[small_num] = 0
        sort_cnt += 1
    small_num -= 1
    large_num -= 1
print(sort_cnt)