N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

def binary_search(list, target):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if list[middle] == target:
            return 1
        elif list[middle] < target:
            lower = middle + 1
        elif list[middle] > target:
            upper = middle - 1
    return 0

for n in check:
    print(binary_search(card, n), end=' ')