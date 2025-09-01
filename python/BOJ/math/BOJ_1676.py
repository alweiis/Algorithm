from math import factorial
cnt = 0
facto = str(factorial(int(input())))
for i in facto[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)