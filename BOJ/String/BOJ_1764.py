from sys import stdin
num1, num2 = map(int, stdin.readline().split())
first_lst = [stdin.readline().rstrip() for _ in range(num1)]
second_lst = [stdin.readline().rstrip() for _ in range(num2)]
result_lst = list(set(first_lst) & set(second_lst))
print(len(result_lst))
for name in sorted(result_lst):
    print(name)