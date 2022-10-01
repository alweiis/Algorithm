from collections import Counter
n = int(input())
first_word = input()
first_counter = Counter(first_word)
answer = 0
for j in range(n-1):
    check_word = input()
    check_counter = Counter(check_word)
    if first_counter == check_counter:
        answer += 1
        continue
    if abs(len(first_word) - len(check_word)) >= 2:
        continue
    wrong_counter = 0
    if len(first_word) >= len(check_word):
        wrong_counter = first_counter - check_counter
    elif len(first_word) < len(check_word):
        wrong_counter = check_counter - first_counter
    if len(wrong_counter) == 0 or (len(wrong_counter) == 1 and wrong_counter.most_common(1)[0][1] < 2):
        answer += 1
print(answer)