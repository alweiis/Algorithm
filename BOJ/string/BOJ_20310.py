s = list(input())
zero_cnt, one_cnt = s.count('0') // 2, s.count('1') // 2
for _ in range(zero_cnt):
    s = s[::-1]
    s.remove('0')
    s = s[::-1]
for _ in range(one_cnt):
    s.remove('1')
print(''.join(s))