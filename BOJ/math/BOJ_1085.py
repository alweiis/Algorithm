x, y, w, h = map(int, input().split())
check = [x, y, w - x, h - y]
print(min(check))