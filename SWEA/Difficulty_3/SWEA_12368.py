T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    time = a + b
    if time >= 24:
        time -= 24
    print(f'#{test_case} {time}')