def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, total + 1):
        column = i
        row = total // column
        yellow_column = column - 2
        yellow_row = row - 2
        area = yellow_row * yellow_column
        if area == yellow:
            return [row, column]