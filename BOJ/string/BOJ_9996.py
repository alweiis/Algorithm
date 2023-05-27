num = int(input())
pattern = input().split('*')
length = [len(pattern[0]), len(pattern[1])]
for _ in range(num):
    flag = False
    check = input()
    if check[:length[0]] == pattern[0]:
        check = check[length[0]:]
        if check[-length[1]:] == pattern[1]:
            flag = True
    print('DA' if flag else 'NE')