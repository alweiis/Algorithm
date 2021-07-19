line = input()
answer = ''
for c in line:
    if c.isalpha():
        num = ord(c) + 13
        if c.isupper():
            answer += chr(num - 26 if num > 90 else num)
        elif c.islower():
            answer += chr(num - 26 if num > 122 else num)
    else:
        answer += c
print(answer)