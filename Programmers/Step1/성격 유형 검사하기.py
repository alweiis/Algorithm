def solution(survey, choices):
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    category = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    result_dict = {c: 0 for c in category}
    for i in range(len(survey)):
        m = choices[i]
        if m == 4:
            continue
        elif m < 4:
            result_dict[survey[i][0]] += score[m]
        elif m > 4:
            result_dict[survey[i][1]] += score[m]
    result_list = list(result_dict.values())
    answer = ''
    for i in range(0, 8, 2):
        if result_list[i] >= result_list[i+1]:
            answer += category[i]
        elif result_list[i] < result_list[i+1]:
            answer += category[i+1]
    return answer