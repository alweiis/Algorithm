T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {a * b}')