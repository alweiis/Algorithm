words = input()
tmp_words = ""
for c in words:
    tmp_words += c
    if len(tmp_words) == 10:
        print(tmp_words)
        tmp_words = ""
else:
    if tmp_words != "":
        print(tmp_words)