from collections import defaultdict

def solution(k, tangerine):
    box_dict = defaultdict(int)
    for num in tangerine:
        box_dict[num] += 1
    box_list = [(num, cnt) for num, cnt in box_dict.items()]
    box_list.sort(key=lambda x: -x[1])
    answer = set()
    for num, cnt in box_list:
        if k > 0:
            answer.add(num)
            k -= cnt
        else:
            break
    return len(answer)