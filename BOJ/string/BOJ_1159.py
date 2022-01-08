name_list = [input()[0] for _ in range(int(input()))]
name_set = set(name_list)
answer = []
for c in name_set:
    if name_list.count(c) >= 5:
        answer.append(c)
if answer:
    print(''.join(sorted(answer)))
else:
    print('PREDAJA')