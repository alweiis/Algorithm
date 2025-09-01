S = input()
T = input()
while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = ''.join(reversed(T))
        if T[0] == 'B':
            T = T[1:]
        else:
            break
print(1 if S == T else 0)