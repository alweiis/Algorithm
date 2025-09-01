text = input()
word = input()
length = len(word)
count = 0
while True:
    i = text.find(word)
    if i >= 0:
        count += 1
        text = text[i+length:]
    else:
        break
print(count)