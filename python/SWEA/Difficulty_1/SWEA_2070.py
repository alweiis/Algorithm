T = int(input())
for i in range(1, T + 1):
    num1, num2 = map(int, input().split())
    flag = '<' if num1 < num2 else ('>' if num1 > num2 else '=')
    print('#{} {}'.format(i, flag))