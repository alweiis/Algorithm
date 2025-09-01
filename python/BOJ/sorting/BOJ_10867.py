N = int(input())
nums = sorted(set(map(int, input().split())))
for number in nums:
    print(number, end=' ')