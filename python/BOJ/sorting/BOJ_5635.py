n = int(input())
info = []
for _ in range(n):
    name, day, month, year = input().split()
    info.append([name, int(year), int(month), int(day)])
info.sort(key=lambda x: (x[1], x[2], x[3]))
print(info[-1][0])
print(info[0][0])