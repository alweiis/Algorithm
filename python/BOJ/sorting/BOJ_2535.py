N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
scores.sort(key=lambda x: -x[2])
answer = [[scores[0][0], scores[0][1]], [scores[1][0], scores[1][1]]]
for i in range(2, N):
    if answer[0][0] == answer[1][0] == scores[i][0]:
        continue
    answer.append([scores[i][0], scores[i][1]])
    break
for nation_num, student_num in answer:
    print(nation_num, student_num)