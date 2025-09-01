n = int(input())
trees = list(map(int, input().split()))
plus = list(map(int, input().split()))
check = []
answer = 0
for tree, grow in zip(trees, plus):
    check.append((tree, grow))
check.sort(key= lambda x:(x[1]))
for i in range(n):
    answer += check[i][0] + check[i][1] * i
print(answer)