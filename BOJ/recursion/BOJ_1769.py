def check_multiple(n, m):
    if len(str(n)) == 1:
        print(m)    # 변환 횟수
        print('YES' if int(n) % 3 == 0 else 'NO')
        return
    n = sum(map(int, list(str(n))))
    check_multiple(n, m + 1)

num = input()
check_multiple(num, 0)
