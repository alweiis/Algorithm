T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    word = input()
    answer = 'No'
    if num % 2 == 0:
        idx = num // 2
        a, b = word[:idx], word[idx:]
        if a == b:
            answer = 'Yes'
    print(f'#{test_case} {answer}')