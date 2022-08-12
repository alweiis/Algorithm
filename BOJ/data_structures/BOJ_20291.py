from collections import defaultdict
n = int(input())
check = defaultdict(int)
result = []
for _ in range(n):
    data = input().split('.')
    check[data[1]] += 1
for key, value in check.items():
    result.append((key, value))
result.sort(key=lambda x: x[0])
for extension, count in result:
    print(f'{extension} {count}')