n = int(input())

for i in range(n):
    score = 0
    o_count = 1
    lst = list(input())
    for j in range(len(lst)):
        if lst[j] == 'O':
            score += o_count
            o_count += 1
        else:
            o_count = 1
    print(score)