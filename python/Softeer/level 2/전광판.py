import sys
input = sys.stdin.readline

bulb = {
    '0': '1110111', '1': '0010010', '2': '1011101',
    '3': '1011011', '4': '0111010', '5': '1101011',
    '6': '1101111', '7': '1110010', '8': '1111111',
    '9': '1111011', ' ': '0000000'
}

t = int(input())
for _ in range(t):
    a, b = input().rstrip().split()
    answer = 0
    while len(a) < 5:
        a = ' ' + a
    while len(b) < 5:
        b = ' ' + b
    for i in range(5):
        for j in range(7):
            if bulb[a[i]][j] != bulb[b[i]][j]:
                answer += 1
    print(answer)