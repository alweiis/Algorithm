n = int(input())
for _ in range(n):
    word = input()
    for c in word:
        word_cnt = word.count(c)
        if word_cnt > 1:
            s_idx, e_idx = word.index(c), word.rindex(c)
            set_word = set(word[s_idx:e_idx + 1])
            if len(set_word) > 1:
                n -= 1
                break
print(n)
