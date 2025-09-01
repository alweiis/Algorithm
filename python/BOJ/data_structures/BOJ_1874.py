from sys import stdin
n = int(stdin.readline())
exp_arr = [int(stdin.readline()) for _ in range(n)]
tmp_arr = [i for i in range(n, 0, -1)]

def chk_stack(exp, tmp):
    stack, chk_arr = [], []
    result = ''
    for i in range(len(exp)):
        while tmp:
            if stack and exp[i] == stack[-1]:
                chk_arr.append(stack.pop())
                result += '-'
                break
            stack.append(tmp.pop())
            result += '+'
        else:
            chk_arr.append(stack.pop())
            result += '-'
    if exp == chk_arr:
        print('\n'.join(result))
    else:
        print('NO')

chk_stack(exp_arr, tmp_arr)