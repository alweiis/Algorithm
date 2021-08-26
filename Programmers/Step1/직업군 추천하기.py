def solution(table, languages, preference):
    new_table, score_list, result_lst = [], [], []

    for row in table:
        new_table.append(list(reversed(row.split())))

    for row in new_table:
        total_score = 0
        for idx in range(len(languages)):
            for score, name in enumerate(row, 1):
                if languages[idx] == name:
                    total_score += score * preference[idx]
        score_list.append(total_score)

    for idx, value in enumerate(score_list):
        if value == max(score_list):
            result_lst.append(new_table[idx][-1])

    return sorted(result_lst)[0]