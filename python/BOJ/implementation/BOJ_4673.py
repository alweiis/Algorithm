not_self_numbers = set()
all_numbers = set([i for i in range(1, 10000 + 1)])

for num in range(1, 10000 + 1):
    result = num
    for ele in str(num):
        result += int(ele)
    not_self_numbers.add(result)

for self_num in sorted(all_numbers - not_self_numbers):
    print(self_num)