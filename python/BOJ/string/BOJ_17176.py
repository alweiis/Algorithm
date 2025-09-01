n = int(input())
password = list(map(int, input().split()))
data = input()
result = []
for c in data:
    if c.isspace():
        result.append(0)
    elif c.islower():
        result.append(ord(c) - 70)
    elif c.upper():
        result.append(ord(c) - 64)
if sorted(password) == sorted(result):
    print('y')
else:
    print('n')