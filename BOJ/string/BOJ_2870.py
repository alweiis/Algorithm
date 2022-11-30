n = int(input())
numbers = []
for _ in range(n):
    data = input()
    check = ''
    for c in data:
        if c.isdigit():
            check += c
        else:
            if check != '':
                numbers.append(int(check))
                check = ''
    else:
        if check != '':
            numbers.append(int(check))
numbers.sort()
for num in numbers:
    print(num)