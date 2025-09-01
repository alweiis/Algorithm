n = int(input())
signal = input()
m = n // 5
tmp = ''
d_signal, check = [], []
numbers = [
    ['#####', '#...#', '#####'],    # 0
    ['#####'],                      # 1
    ['#.###', '#.#.#', '###.#'],    # 2
    ['#.#.#', '#.#.#', '#####'],    # 3
    ['###..', '..#..', '#####'],    # 4
    ['###.#', '#.#.#', '#.###'],    # 5
    ['#####', '#.#.#', '#.###'],    # 6
    ['#....', '#....', '#####'],    # 7
    ['#####', '#.#.#', '#####'],    # 8
    ['###.#', '#.#.#', '#####'],    # 9
]
for i, c in enumerate(signal, start=1):
    tmp += c
    if i % m == 0:
        d_signal.append(list(tmp) + ['.'])
        tmp = ''
# 2차원 배열 뒤집기
d_signal = list(map(list, zip(*d_signal)))
answer = ''
for a in d_signal:
    letters = ''.join(a)
    if letters != '.....':
        check.append(letters)
    else:
        if check:
            for idx in range(10):
                if check == numbers[idx]:
                    answer += str(idx)
                    check = []
print(answer)