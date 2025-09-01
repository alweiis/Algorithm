def solution(park, routes):
    height, width = len(park), len(park[0])
    x, y = -1, -1
    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        op, n = route.split()
        n = int(n)
        if op == 'E':
            if y + n > width - 1:
                continue
            for j in range(y + 1, y + n + 1):
                if park[x][j] == 'X':
                    break
            else:
                y += n
        elif op == 'W':
            if y - n < 0:
                continue
            for j in range(y - 1, y - n - 1, -1):
                if park[x][j] == 'X':
                    break
            else:
                y -= n
        elif op == 'N':
            if x - n < 0:
                continue
            for i in range(x - 1, x - n - 1, -1):
                if park[i][y] == 'X':
                    break
            else:
                x -= n
        elif op == 'S':
            if x + n > height - 1:
                continue
            for i in range(x + 1, x + n + 1):
                if park[i][y] == 'X':
                    break
            else:
                x += n
    answer = [x, y]
    return answer