from collections import Counter
from sys import stdin
n = int(stdin.readline())
nums = sorted([int(stdin.readline()) for _ in range(n)])
# 산술평균 출력
print(round(sum(nums)/n))
# 중앙값 출력
print(nums[(n//2)])
# 최빈값 출력
count_list = Counter(nums).most_common(2)
if len(count_list) > 1 and count_list[0][1] == count_list[1][1]:
    print(count_list[1][0])
else:
    print(count_list[0][0])
# 범위 출력
print(max(nums)-min(nums))