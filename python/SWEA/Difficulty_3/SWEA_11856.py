T = int(input())
for test_case in range(1, T+1):
    check = set(list(input()))
    answer = 'Yes' if len(check) == 2 else 'No'
    print(f'#{test_case} {answer}')