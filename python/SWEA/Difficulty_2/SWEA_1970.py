T = int(input())
for test_case in range(1, T + 1):
    types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = int(input())
    arr = [0] * 8
    for i in range(8):
        arr[i] = money // types[i]
        money = money % types[i]
    print(f'#{test_case}')
    print(*arr)