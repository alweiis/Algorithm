num_list = [int(input()) for x in range(7)]
odd_list = []
for index in range(len(num_list)):
    if num_list[index] % 2 == 1:
        odd_list.append(num_list[index])
if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list))
    print(min(odd_list))
