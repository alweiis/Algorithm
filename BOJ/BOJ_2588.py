a = int(input())
b = int(input())

lst = []
for i in reversed(str(b)):
    lst.append(i)
    print(a * int(i))
print(a * b)
