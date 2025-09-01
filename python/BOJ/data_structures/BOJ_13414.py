import sys
input = sys.stdin.readline
k, l = map(int, input().split())
student = {}
order = 0
for _ in range(l):
    number = input().rstrip()
    student[number] = order
    order += 1
answer = [(number, order) for number, order in student.items()]
answer.sort(key=lambda x: x[1])
k = min(k, len(answer))
for i in range(k):
    print(answer[i][0])