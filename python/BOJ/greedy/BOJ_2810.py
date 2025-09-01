n = int(input())
seat = input()
cup = 1 + n - seat.count("LL")
print(min(cup, n))