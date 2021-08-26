def solution(table, languages, preference):
    new_table, score_list, result_lst = [], [], []

    for line in table:
        new_table.append(list(reversed(line.split())))

    for line in new_table:
        score = 0
        for i in range(len(languages)):
            for j, name in enumerate(line, 1):
                if languages[i] == name:
                    score += j * preference[i]
        score_list.append(score)

    for i, value in enumerate(score_list):
        if value == max(score_list):
            result_lst.append(new_table[i][-1])

    return sorted(result_lst)[0]
