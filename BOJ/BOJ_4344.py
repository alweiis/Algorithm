n = int(input())
for i in range(n):
    student_cnt = 0
    student_num, *student_score = map(int, input().split())
    score_avg = sum(student_score) / student_num
    for each_score in student_score:
        if each_score > score_avg:
            student_cnt += 1
    print("{:.3f}%".format(student_cnt / student_num * 100))
