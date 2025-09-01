from collections import defaultdict
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    terms_dic = defaultdict(int)
    for s in terms:
        alphabet, month = s.split()
        terms_dic[alphabet] = int(month)

    for index, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        current_date = [int(x) for x in date.split('.')]
        year_to_add, month_to_add = divmod(terms_dic[term], 12)
        current_date[0] += year_to_add
        current_date[1] += month_to_add

        if current_date[1] > 12:
            year, month = divmod(current_date[1], 12)
            current_date[0] += year
            current_date[1] = month
        if current_date[2] == 1:
            if current_date[1] == 1:
                current_date[1] = 12
            else:
                current_date[1] -= 1
            current_date[2] = 28
        else:
            current_date[2] -= 1

        today_date = datetime.strptime(today, "%Y.%m.%d")
        calc_date = datetime.strptime(f'{current_date[0]}.{current_date[1]}.{current_date[2]}', "%Y.%m.%d")
        if calc_date < today_date:
            answer.append(index)
    answer.sort()
    return answer