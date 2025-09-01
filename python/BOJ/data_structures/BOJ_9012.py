from sys import stdin
def check_vps(string):
    stack_lst = []
    for sign in string:
        if sign == '(':
            stack_lst.append(sign)
        else:
            if len(stack_lst) == 0:
                return 'NO'
            stack_lst.pop()
    return 'YES' if len(stack_lst) == 0 else 'NO'

t = int(stdin.readline())
for _ in range(t):
    print(check_vps(stdin.readline().rstrip()))
