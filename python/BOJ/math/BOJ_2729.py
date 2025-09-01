n = int(input())
for _ in range(n):
    num1, num2 = input().split()
    length1, length2 = len(num1), len(num2)
    length = max(length1, length2)
    diff = length1 - length2
    tmp = 0
    result = ''
    if diff > 0:
        num2 = ('0' * diff) + num2
    elif diff < 0:
        num1 = ('0' * abs(diff)) + num1
    for i in range(length - 1, -1, -1):
        number = int(num1[i]) + int(num2[i]) + tmp
        if number == 3:
            tmp = 1
            result = '1' + result
        elif number == 2:
            tmp = 1
            result = '0' + result
        else:
            tmp = 0
            result = str(number) + result
    if tmp == 1:
        result = str(tmp) + result
    print(int(result))