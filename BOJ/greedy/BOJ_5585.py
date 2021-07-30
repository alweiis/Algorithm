price = int(input())
money = 1000 - price
coin_arr = [500, 100, 50, 10, 5, 1]
cnt = 0
while money:
    for coin in coin_arr:
        cnt += money // coin
        money = money % coin
print(cnt)