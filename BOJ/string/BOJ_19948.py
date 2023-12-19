contents = input()
space_cnt = int(input())
alphabets = list(map(int, input().split()))

capitals = ''.join([word[0] for word in contents.split()])
tmp_str = ''
recordable = True
for c in capitals:
    if tmp_str == c:
        continue
    tmp_str = c
    k = ord(c.lower()) - ord('a')
    if alphabets[k] > 0:
        alphabets[k] -= 1
    else:
        recordable = False

tmp_str = ''
for c in contents:
    if tmp_str == c:
        continue
    tmp_str = c
    if c.isalpha():
        k = ord(c.lower()) - ord('a')
        if alphabets[k] > 0:
            alphabets[k] -= 1
        else:
            recordable = False
    else:
        if space_cnt > 0:
            space_cnt -= 1
        else:
            recordable = False

print(capitals.upper() if recordable else -1)