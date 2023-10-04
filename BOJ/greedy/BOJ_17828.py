N, X = map(int, input().split())
if 26 * N < X or N > X:
    print('!')
else:
    answer = ['A'] * N
    X -= N
    idx = N - 1
    while X > 0:
        if X >= 25:
            answer[idx] = 'Z'
            idx -= 1
            X -= 25
        else:
            answer[idx] = chr(X + 65)
            break
    print(''.join(answer))