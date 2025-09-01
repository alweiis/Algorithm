board = input()
if board.count('X') % 2 != 0:
    answer = -1
else:
    x_cnt = 0
    answer = ''
    for i in range(len(board)):
        if board[i] == 'X':
            x_cnt += 1
            if x_cnt == 4:
                answer += 'AAAA'
                x_cnt = 0
        else:
            if x_cnt == 2:
                answer += 'BB'
                x_cnt = 0
            elif x_cnt % 2 == 1:
                answer = -1
                break
            answer += '.'
    else:
        if x_cnt == 2:
            answer += 'BB'
print(answer)