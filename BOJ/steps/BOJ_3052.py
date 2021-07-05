s = set()
for i in range(10):
    a = int(input())
    s.add(a % 42)
print(len(s))
