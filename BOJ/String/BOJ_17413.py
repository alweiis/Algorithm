S = input()
result, tmp = [], []
for c in S:
    if c == ' ':
        if '<' in tmp:
            tmp.append(c)
        else:
            result.extend(reversed(tmp))
            result.append(c)
            tmp.clear()
    elif c == '>':
        tmp.append(c)
        result.extend(tmp)
        tmp.clear()
    elif c == '<':
        if tmp:
            result.extend(reversed(tmp))
            tmp.clear()
        tmp.append(c)
    else:
        tmp.append(c)
if tmp:
    result.extend(reversed(tmp))
print(''.join(result))