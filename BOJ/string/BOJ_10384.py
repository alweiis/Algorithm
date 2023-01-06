from collections import defaultdict
for i in range(1, int(input()) + 1):
    data = input().lower()
    checker = defaultdict(int)
    for c in data:
        if c.isalpha():
            checker[c] +=1
    if len(checker) < 26:
        print(f'Case {i}: Not a pangram')
    else:
        n = min(checker.values())
        if n == 1:
            print(f'Case {i}: Pangram!')
        elif n == 2:
            print(f'Case {i}: Double pangram!!')
        else:
            print(f'Case {i}: Triple pangram!!!')