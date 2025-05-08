while True:
    word = input()
    if word == '#':
        break
    one = 0
    result = ''
    for i in range(len(word)):
        if word[i] == 'e':
            if one % 2 == 1:
                result += '1'
            else:
                result += '0'
        elif word[i] == 'o':
            if one % 2 == 1:
                result += '0'
            else:
                result += '1'
        else:
            result += word[i]
            if word[i] == '1':
                one += 1
    print(result)