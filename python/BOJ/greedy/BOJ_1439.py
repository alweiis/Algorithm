def change_string(x, a, b):
    cnt = 0
    for i in range(len(x)):
        if x[i] == b and x[i - 1] == a:
            cnt += 1
    print(cnt)

strings = input()
zero_cnt, one_cnt = strings.count('0'), strings.count('1')

if zero_cnt >= one_cnt:
    change_string(strings, '1', '0')
else:
    change_string(strings, '0', '1')