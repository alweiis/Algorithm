def solution(keymap, targets):
    checker = {}
    answer = []
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in checker:
                checker[key[i]] = i + 1
            else:
                checker[key[i]] = min(checker[key[i]], i + 1)
    for target in targets:
        count = 0
        for x in target:
            if x not in checker.keys():
                answer.append(-1)
                break
            else:
                count += checker[x]
        else:
            answer.append(count)
    return answer