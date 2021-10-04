count = int(input())
a_list = sorted(map(int, input().split()))
if count == 1:
    print(a_list[0] ** 2)
else:
    print(a_list[0] * a_list[-1])