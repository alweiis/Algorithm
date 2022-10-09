from collections import deque
n = int(input())
checker = set()
checker.add(''.join(input()))
for _ in range(n-1):
    word = deque(input())
    for _ in range(len(word)):
        tmp = ''.join(word)
        if tmp in checker:
            break
        word.rotate()
    else:
        checker.add(''.join(word))
print(len(checker))