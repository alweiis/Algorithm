n = int(input())
budget = sorted(map(int, input().split()))
m = int(input())
if sum(budget) <= m:
    print(budget[-1])
else:
    left, right = 1, budget[-1]
    answer = 1
    while left <= right:
        middle = (left + right) // 2
        result = 0
        for money in budget:
            if money <= middle:
                result += money
            else:
                result += middle
        if result > m:
            right = middle - 1
        else:
            left = middle + 1
            answer = max(answer, middle)
    print(answer)