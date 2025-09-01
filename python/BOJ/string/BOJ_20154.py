from collections import deque
from string import ascii_uppercase
number = '32123333113133122212112221'
table = {}
for i in range(len(number)):
    table[ascii_uppercase[i]] = number[i]
s = input()
q = deque([int(table[c]) for c in s])
while len(q) > 1:
    num1 = q.popleft()
    num2 = q.popleft()
    num = num1 + num2
    if num >= 10:
        num %= 10
    q.appendleft(num)
if q[0] % 2 == 0:
    print('You\'re the winner?')
else:
    print('I\'m a winner!')