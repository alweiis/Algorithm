w, n = map(int, input().split())
jewel = [tuple(map(int, input().split())) for _ in range(n)]
jewel.sort(key=lambda x:-x[1])
bag_weight, price = 0, 0
for jewel_weight, jewel_price in jewel:
    if bag_weight == w:
        break
    if bag_weight + jewel_weight <= w:
        bag_weight += jewel_weight
        price += (jewel_weight * jewel_price)
    else:
        tmp_weight = w - bag_weight
        bag_weight += tmp_weight
        price += (tmp_weight * jewel_price)
print(price)