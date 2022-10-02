word = input()
answer = 0
if len(word) % 4 != 0:
    print(answer)
    exit()
if word.count('w') != word.count('o'):
    print(answer)
    exit()
w, o, l, f = '', '', '', ''
for c in word:
    if c == 'w':
        w += c
        if len(o) > 0 or len(l) > 0 or len(f) > 0:
            break
    elif c == 'o':
        if len(w) == 0:
            break
        o += c
    elif c == 'l':
        if len(w) != len(o):
            break
        l += c
    elif c == 'f':
        if len(w) != len(o) or len(o) != len(l):
            break
        f += c
    if len(w) == len(o) == len(l) == len(f):
        w, o, l, f = '', '', '', ''
else:
    if w == o == l == f == '':
        answer = 1
print(answer)