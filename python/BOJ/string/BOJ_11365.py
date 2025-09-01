from sys import stdin
while True:
    code = stdin.readline().rstrip()
    if code == 'END':
        break
    print(code[::-1])