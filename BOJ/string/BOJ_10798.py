word_lst = [input() for _ in range(5)]
list_length = [len(word_lst[i]) for i in range(5)]
max_num = max(list_length)  # 리스트의 원소중 가장 긴 길이
for i in range(5):
    while len(word_lst[i]) < max_num:
        word_lst[i] += '-'
word_lst = list(map(list, zip(*word_lst)))
answer = ''
for words in word_lst:
    for c in words:
        answer += c
print(answer.replace('-', ''))