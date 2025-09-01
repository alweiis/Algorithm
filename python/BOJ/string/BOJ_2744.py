import string
chk_string = input()
answer = ''
for i in range(len(chk_string)):
    if chk_string[i] in string.ascii_lowercase:
        answer += chk_string[i].upper()
    else:
        answer += chk_string[i].lower()
print(answer)