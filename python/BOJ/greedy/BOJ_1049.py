n, m = map(int, input().split())
packages, pieces, answer = [], [], []
for _ in range(m):
    package_price, piece_price = map(int, input().split())
    packages.append(package_price)
    pieces.append(piece_price)
packages.sort()
pieces.sort()
if n <= 6:
    answer.append(packages[0])
    answer.append(pieces[0] * n)
else:
    a, b = divmod(n, 6)
    answer.append(packages[0] * a + pieces[0] * b)
    answer.append(packages[0] * (a + 1))
    answer.append(pieces[0] * n)
print(min(answer))