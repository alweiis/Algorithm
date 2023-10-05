n = int(input())
words = [input() for _ in range(n)]
checker = {' '}
answer = []
for word in words:
    changed = False
    tmp = word.split()
    for i in range(len(tmp)):
        if tmp[i][0].upper() not in checker:
            checker.add(tmp[i][0].upper())
            tmp[i] = '[' + tmp[i][0] + ']' + tmp[i][1:]
            answer.append(' '.join(tmp))
            changed = True
            break
    if not changed:
        for i in range(len(word)):
            if word[i].upper() not in checker:
                checker.add(word[i].upper())
                answer.append(word[:i] + '[' + word[i] + ']' + word[i+1:])
                changed = True
                break
    if not changed:
        answer.append(word)
for word in answer:
    print(word)