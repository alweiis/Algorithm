word = input().upper()
word_cnt = dict()
for c in word:
    if c in word_cnt:
        word_cnt[c] += 1
    else:
        word_cnt[c] = 1

answer = [k for k, v in word_cnt.items() if max(word_cnt.values()) == v]
if len(answer) > 1:
    print('?')
else:
    print(answer[0])