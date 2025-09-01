n, b = input().split()
b = int(b)
real_num, cnt = 0, 0
for ele in reversed(n):
    ele = int(ele) if ele.isdigit() else ord(ele) - 55
    real_num += ele * (b ** cnt)
    cnt += 1
print(real_num)