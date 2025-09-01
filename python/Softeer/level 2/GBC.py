import sys
input = sys.stdin.readline

n, m = map(int, input().split())
standard = [list(map(int, input().split())) for _ in range(n)]
record = [list(map(int, input().split())) for _ in range(m)]
s_pnt, r_pnt = 0, 0
answer = 0
s_boundary = standard[s_pnt][0]
r_boundary = record[r_pnt][0]
for section in range(1, 101):
    while section > s_boundary:
        s_pnt += 1
        s_boundary += standard[s_pnt][0]
    while section > r_boundary:
        r_pnt += 1
        r_boundary += record[r_pnt][0]
    standard_speed = standard[s_pnt][1]
    record_speed = record[r_pnt][1]
    if standard_speed < record_speed:
        answer = max(answer, record_speed - standard_speed)
print(answer)