def calculate_weight(n):
    answer = []
    if n % 3 == 0:
        answer.append(n // 3)
    if n % 5 == 0:
        answer.append(n // 5)

    n1, n2 = n, n
    i, j = 0, 0
    while n1 - 5 > 0:
        n1 -= 5
        i += 1
        if n1 % 3 == 0:
            answer.append(i + (n1 // 3))
    while n2 - 3 > 0:
        n2 -= 3
        j += 1
        if n2 % 5 == 0:
            answer.append(j + (n2 // 5))

    if answer:
        return min(answer)
    else:
        return -1

N = int(input())
print(calculate_weight(N))