n = int(input())
s = input()
if n % 2 == 1:
    print(-1)
else:
    count = 0
    while s:
        stack = []
        s1, s2 = s, s
        s1 = s1.replace('()', 'O')
        s1 = s1.replace(')(', 'X')
        s2 = s2.replace(')(', 'X')
        s2 = s2.replace('()', 'O')
        s = s1 if len(s1) < len(s2) else s2
        for c in s:
            if c == '(' or c == ')':
                stack.append(c)
        if stack.count('(') != stack.count(')'):
            print(-1)
            exit(0)
        s = ''.join(stack)
        count += 1
    print(count)