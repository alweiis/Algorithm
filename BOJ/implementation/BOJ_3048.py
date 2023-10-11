n1, n2 = map(int, input().split())
left = list(reversed(input()))
right = list(input())
t = int(input())
match = left + right
m = n1 + n2
for _ in range(t):
    changed = [False] * m
    for j in range(m - 1):
        if match[j] in left and match[j+1] in right:
            if not changed[j] and not changed[j+1]:
                match[j], match[j+1] = match[j+1], match[j]
                changed[j], changed[j+1] = True, True
print(''.join(match))