a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
all_list = [a, b, c]
for i in range(len(all_list)):
    count = 0
    for j in all_list[i]:
        if j == 0:
            count += 1
    if count == 1:
        print('A')
    elif count == 2:
        print('B')
    elif count == 3:
        print('C')
    elif count == 4:
        print('D')
    else:
        print('E')

