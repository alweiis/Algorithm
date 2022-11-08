from collections import deque
s = input()
key = deque(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
password = ''
for c in s:
    if c.isspace():
        password += ' '
    else:
        password += alphabet[ord(c) - ord(key[0]) - 1]
    key.rotate(-1)
print(password)