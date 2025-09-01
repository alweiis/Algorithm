import itertools
n = 5
bingo_board = [list(map(int, input().split())) for _ in range(n)]
chk_board = [list(map(int, input().split())) for _ in range(n)]
numbers = list(itertools.chain(*chk_board))    # 1차원 배열로 변경
chk_num = 0    # 사회자가 부른 횟수

def chk_bingo(arr):
    bingo = 0
    for i in range(n):  # 가로줄 확인
        if sum(arr[i]) == 0:
            bingo += 1
    new_arr = list(map(list, zip(*arr))) # 2차원 배열 뒤집기
    for i in range(n):  # 세로줄 확인
        if sum(new_arr[i]) == 0:
            bingo += 1
    diagonal = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4]
    if diagonal == 0:   # 대각선 확인 - 1
        bingo += 1
    diagonal_ = arr[4][0] + arr[3][1] + arr[2][2] + arr[1][3] + arr[0][4]
    if diagonal_ == 0:  # 대각선 확인 - 2
        bingo += 1
    return bingo

for number in numbers:
    for i in range(n):
        for j in range(n):
            if number == bingo_board[i][j]:
                bingo_board[i][j] = 0
                chk_num += 1
                bingo = chk_bingo(bingo_board)
                if bingo >= 3:
                    print(chk_num)
                    exit()