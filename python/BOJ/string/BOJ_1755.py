check_string = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
                "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"}
m, n = map(int, input().split())
answer = []
for number in range(m, n + 1):
    tmp = [check_string[c] for c in str(number)]
    string = ' '.join(tmp)
    answer.append((string, number))
answer.sort(key=lambda x: x[0])
count = 0
for _, number in answer:
    print(number, end=' ')
    count += 1
    if count == 10:
        print()
        count = 0