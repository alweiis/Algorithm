import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
secret_op = list(map(int, input().split()))
user_op = list(map(int, input().split()))
answer = 'normal'

if n < m:
    print(answer)
else:
    for i in range(n - m + 1):
        if user_op[i:i + m] == secret_op:
            answer = 'secret'
    print(answer)