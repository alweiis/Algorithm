def solution(wallpaper):
    left, top = float('inf'), float('inf')
    right, bottom = float('-inf'), float('-inf')
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                left = min(left, i)
                top = min(top, j)
                right = max(right, i + 1)
                bottom = max(bottom, j + 1)
    answer = [left, top, right, bottom]
    return answer