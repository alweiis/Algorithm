n = int(input())
init_lst = [tuple(map(int, input().split())) for _ in range(n)]
body_rank = []
length = len(init_lst)
for i in range(length):
    rank = 1
    for j in range(length):
        if init_lst[i][0] < init_lst[j][0] and init_lst[i][1] < init_lst[j][1]:
            rank += 1
    body_rank.append(rank)
print(" ".join(map(str, body_rank)))
