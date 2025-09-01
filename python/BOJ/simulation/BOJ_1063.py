chess_column = {chr(i + 65): i for i in range(8)}
board = [[0] * 8 for _ in range(8)]
k_loc, s_loc, n = input().split()
k_loc, s_loc = list(k_loc), list(s_loc)

king_x, king_y = abs(int(k_loc[1]) - 8), chess_column[k_loc[0]]
stone_x, stone_y = abs(int(s_loc[1]) - 8), chess_column[s_loc[0]]

board[king_x][king_y] = 1
board[stone_x][stone_y] = 2

def move(a, b, c, d):
    global king_x, king_y, stone_x, stone_y
    if 0 <= a < 8 and 0 <= b < 8:
        if board[a][b] == 0:
            board[a][b], board[king_x][king_y] = board[king_x][king_y], board[a][b]
            king_x, king_y = a, b
        elif board[a][b] == 2:
            if 0 <= c < 8 and 0 <= d < 8:
                board[c][d], board[stone_x][stone_y] = board[stone_x][stone_y], board[c][d]
                stone_x, stone_y = c, d
                board[a][b], board[king_x][king_y] = board[king_x][king_y], board[a][b]
                king_x, king_y = a, b

for _ in range(int(n)):
    command = input()
    if command == 'L':
        move(king_x, king_y - 1, stone_x, stone_y - 1)
    if command == 'R':
        move(king_x, king_y + 1, stone_x, stone_y + 1)
    if command == 'T':
        move(king_x - 1, king_y, stone_x - 1, stone_y)
    if command == 'B':
        move(king_x + 1, king_y, stone_x + 1, stone_y)
    if command == 'LB':
        move(king_x + 1, king_y - 1, stone_x + 1, stone_y - 1)
    if command == 'RB':
        move(king_x + 1, king_y + 1, stone_x + 1, stone_y + 1)
    if command == 'LT':
        move(king_x - 1, king_y - 1, stone_x - 1, stone_y - 1)
    if command == 'RT':
        move(king_x - 1, king_y + 1, stone_x - 1, stone_y + 1)

print(chr(king_y + 65) + str(abs(king_x - 8)))
print(chr(stone_y + 65) + str(abs(stone_x - 8)))