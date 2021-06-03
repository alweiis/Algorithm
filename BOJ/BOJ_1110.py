a = input()
count = 0
c = a

while True:
    if int(c) < 10:
        c = '0' + c
    # print("C1:", c)
    b = int(c[0]) + int(c[-1])
    # print("B:", b)
    c = str(c[-1]) + str(b)[-1]
    # print("C2:", c)
    count += 1
    # print("COUNT:", count)
    if int(a) == int(c):
        print(count)
        break
