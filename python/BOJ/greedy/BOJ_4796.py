import sys
input = sys.stdin.readline

case_num = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    a, b = divmod(V, P)
    if b < L:
        usable_days = a * L + b
    else:
        usable_days = a * L + L
    print(f'Case {case_num}: {usable_days}')
    case_num += 1