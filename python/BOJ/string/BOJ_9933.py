N = int(input())
password_list = [input() for _ in range(N)]
for chk_word in password_list:
    reversed_word = chk_word[::-1]
    if reversed_word in password_list:
        idx = len(reversed_word)
        print(idx, reversed_word[idx // 2])
        break