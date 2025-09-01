from sys import stdin

word = stdin.readline().rstrip()
chk = ''
m = int(stdin.readline())
for _ in range(m):
    order = stdin.readline().rstrip()
    if len(order) >= 2:
        order, c = order.split()
        word += c
    else:
        if order == 'L' and word:
            chk += word[-1]
            word = word[:-1]
        elif order == 'D' and chk:
            word += chk[-1]
            chk = chk[:-1]
        elif order == 'B':
            word = word[:-1]
if chk:
    word += chk[::-1]
print(word)