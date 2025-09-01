def solution(answers):
    answer = []
    count_one, count_two, count_three = 0, 0, 0
    answer_one = [1, 2, 3, 4, 5]
    answer_two = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == answer_one[i % len(answer_one)]:
            count_one += 1
        if answers[i] == answer_two[i % len(answer_two)]:
            count_two += 1
        if answers[i] == answer_three[i % len(answer_three)]:
            count_three += 1

    answer_temp = [count_one, count_two, count_three]

    for number, score in enumerate(answer_temp, 1):
        if score == max(answer_temp):
            answer.append(number)
    return answer