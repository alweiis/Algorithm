def solution(board, moves):
    answer = []
    cnt = 0
    for ele in moves:
        idx = ele - 1
        for i in board:
            if i[idx] != 0:
                answer.append(i[idx])
                i[idx] = 0
                break
        if len(answer) >= 2:
            if answer[-2] == answer[-1]:
                del answer[-2:]
                cnt += 2
    return answer
