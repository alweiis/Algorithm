check = input()
n = int(input())
count = 0
for _ in range(n):
    sentence = input()
    rotate_count = 0
    while rotate_count < 10:
        if check in sentence:
            count += 1
            break
        sentence = sentence[1:] + sentence[0]
        rotate_count += 1
print(count)