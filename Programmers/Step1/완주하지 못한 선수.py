def solution(participant, completion):
    chk_dict = {}
    for man in participant:
        if man in chk_dict:
            chk_dict[man] += 1
        else:
            chk_dict[man] = 1
    for man in completion:
        chk_dict[man] -= 1
    for key, value in chk_dict.items():
        if value == 1:
            return key