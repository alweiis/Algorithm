name = input()
result = ''
for c in name:
    if c.isupper():
        result += c
print(result)