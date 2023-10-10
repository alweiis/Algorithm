def solution(n, words):
    ground = 1
    checker = {words[0]}
    for i in range(1, len(words)):
        failed = False
        if words[i - 1][-1] != words[i][0]:
            failed = True
        if not failed and words[i] in checker:
            failed = True
        if failed:
            return [(i % n) + 1, ground]
        checker.add(words[i])
        if (i + 1) % n == 0:
            ground += 1
    return [0, 0]