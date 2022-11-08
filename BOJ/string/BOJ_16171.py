s = input()
keyword = input()
strings = ''
for c in s:
    if c.isalpha():
        strings += c
print(1 if keyword in strings else 0)