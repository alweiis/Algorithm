# 코드 수정후 업로드(21-06-17)
def solution(lottos, win_nums):
    score_table = [6, 6, 5, 4, 3, 2, 1]
    max_cnt, min_cnt = 0, 0
    for num in lottos:
        if num in win_nums:
            max_cnt += 1
            min_cnt += 1
        if num == 0:
            max_cnt += 1
    answer = [score_table[max_cnt], score_table[min_cnt]]
    print(answer)
    return answer