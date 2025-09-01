n = int(input())
go_in, go_out = {}, {}
for order in range(n):
    car_number = input()
    go_in[order] = car_number
for order in range(n):
    car_number = input()
    go_out[car_number] = order

count = 0
for i in range(1, n):
    for j in range(0, i):
        if go_out[go_in[j]] > go_out[go_in[i]]:
            count += 1
            break
print(count)