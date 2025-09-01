def check(word):
    if 'U' in word:
        i = word.index('U')
        word = word[i+1:]
        if 'C' in word:
            j = word.index('C')
            word = word[j+1:]
            if 'P' in word:
                k = word.index('P')
                word = word[k+1:]
                if 'C' in word:
                    return True
    return False

s = input()
chk = ''
for i in range(len(s)):
    if s[i].isupper():
        chk += s[i]
if check(chk):
    print('I love UCPC')
else:
    print('I hate UCPC')