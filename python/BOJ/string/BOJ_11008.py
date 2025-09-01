for _ in range(int(input())):
    s, p = input().split()
    p_cnt = s.count(p)
    s = s.replace(p, '')
    answer = len(s) + p_cnt
    print(answer)