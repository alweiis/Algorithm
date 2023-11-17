n = int(input())
colors = input() + 'X'
b, r = [], []
count = 1
for i in range(n):
    if colors[i] == colors[i+1]:
        count += 1
    else:
        if colors[i] == 'B':
            b.append(count)
        else:
            r.append(count)
        count = 1
print(1 + len(r) if colors[-2] == 'B' else 1 + len(b))