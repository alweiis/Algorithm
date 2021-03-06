from sys import stdin
books = dict()
n = int(input())
for _ in range(n):
    book = stdin.readline().rstrip('\n')
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1
result = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])