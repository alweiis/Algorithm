n = int(input())
lst = [idx for idx in range(1, n+1)]
while len(lst) > 1:
    lst = [lst[idx] for idx in range(len(lst)) if idx % 2 == 1]
print(lst[0])
