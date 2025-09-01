strings = input()
explosion = input()
n = len(explosion)
stack = []
for c in strings:
    stack.append(c)
    if n <= len(stack):
        tmp = "".join(stack[-n:])
        if tmp == explosion:
            del stack[-n:]  # 뒤에서 부터 n개를 지운다.
if stack:
    print(''.join(stack))
else:
    print('FRULA')