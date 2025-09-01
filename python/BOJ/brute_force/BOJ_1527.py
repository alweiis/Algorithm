from itertools import product
a, b = map(int, input().split())
a_length = len(str(a))
b_length = len(str(b))
count = 0

for i in range(a_length, b_length + 1):
    for n in product([4, 7], repeat=i):
        num = int(''.join(map(str, n)))
        if a <= num <= b:
            count += 1
print(count)
