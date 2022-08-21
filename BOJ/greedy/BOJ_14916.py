N = int(input())
result = []
def check_money(num, a, b):
    chk, r = divmod(num, a)
    if r == 0:
        result.append(chk)
        return
    if chk == 0:
        return
    q1 = 1
    while q1 <= chk:
        q2, r = divmod(num - (a * q1), b)
        if r == 0:
            result.append(q1 + q2)
        q1 += 1
check_money(N, 5, 2)
check_money(N, 2, 5)
if not result:
    print(-1)
else:
    print(min(result))