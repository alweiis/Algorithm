s = input()
length = len(s)
if s == s[::-1]:
    print(length)
else:
    answer = []
    for i in range(length):
        tmp = "".join(reversed(s[:i+1]))
        chk_str = s + tmp
        if chk_str == chk_str[::-1]:
            answer.append(len(chk_str))
    print(min(answer))