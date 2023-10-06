n = int(input())
words = {input() for _ in range(n)}
words = sorted(words, key=lambda x: -len(x))
answer = [words[0]]
for i in range(1, len(words)):
    flag = True
    for j in range(len(answer)):
        count = 0
        for k in range(len(words[i])):
            if words[i][k] == answer[j][k]:
                count += 1
        if count == len(words[i]):
            flag = False
    if flag:
        answer.append(words[i])
print(len(answer))