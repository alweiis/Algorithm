word = input()
result = []
for i in range(len(word)):
    result.append(word[i:])
result.sort()
for eli in result:
    print(eli)