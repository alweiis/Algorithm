n = int(input())

def trim(s):
    s = s.replace(' ', '-')
    answer = ''
    for i in range(len(s)):
        if s[i] == '-':
            if answer[-1] == '-':
                continue
        answer += s[i]
    return answer

def trim_symbols(s):
    symbols = ['(', ')', '[', ']', '{', '}', '.', ',', ';', ':']
    answer = ''
    for i in range(len(s)):
        if s[i] == '-':
            if s[i-1] in symbols or s[i+1] in symbols:
                continue
        answer += s[i]
    return answer

for i in range(n):
    empty_cnt = n - 1
    s1 = input().strip().lower().replace(',', ';')
    s2 = input().strip().lower().replace(',', ';')
    s1 = s1.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')
    s2 = s2.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')
    s1, s2 = trim_symbols(trim(s1)), trim_symbols(trim(s2))
    result = 'equal' if s1 == s2 else 'not equal'
    print(f'Data Set {i+1}: {result}')
    if empty_cnt:
        print()
        empty_cnt -= 1