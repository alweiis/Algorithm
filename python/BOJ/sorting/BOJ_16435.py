_, snake = map(int, input().split())
fruits = sorted(map(int, input().split()))
for fruit in fruits:
    if snake >= fruit:
        snake += 1
print(snake)