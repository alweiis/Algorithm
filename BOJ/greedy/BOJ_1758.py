n = int(input())
order = []
for _ in range(n):
    order.append(int(input()))
order.sort(reverse=True)
answer = 0
for i in range(n):
    money = order[i] - ((i+1) - 1)
    if money > 0:
        answer += money
print(answer)