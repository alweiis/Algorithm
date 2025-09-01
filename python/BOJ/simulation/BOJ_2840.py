import sys
from collections import deque
n, k = map(int, input().split())
circle = deque(['?'] * n)
for _ in range(k):
    spin_cnt, letter = input().split()
    spin_cnt, pop_cnt = int(spin_cnt), 0
    while pop_cnt != spin_cnt:
        c = circle.popleft()
        pop_cnt += 1
        if pop_cnt == spin_cnt:
            if (c == '?' or c == letter) and letter not in circle:
                circle.append(letter)
            else:
                print('!')
                sys.exit()
        else:
            circle.append(c)
print("".join(reversed(circle)))