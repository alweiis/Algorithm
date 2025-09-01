s = input()
answer = set()
n = len(s)
for i in range(n):
    for j in range(n - i):
        x = s[j:j+i+1]
        answer.add(x)
print(len(answer))