n, kind = input().split()
answer = 0
game = {'Y': 1, 'F': 2, 'O': 3}
played, temp = {}, []
for _ in range(int(n)):
    name = input()
    if played.get(name):
        continue
    played[name] = 1
    temp.append(name)
    if game[kind] == len(temp):
        answer += 1
        temp = []
print(answer)