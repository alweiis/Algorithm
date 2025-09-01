from sys import stdin
input = stdin.readline

stack = []
final_score = 0
for _ in range(int(input())):
    arr = input().rstrip().split()
    if len(arr) == 3:
        score, time = int(arr[1]), int(arr[2]) - 1
        if time == 0:
            final_score += score
        else:
            stack.append((score, time))
    else:
        if stack:
            score, time = stack.pop()
            time -= 1
            if time == 0:
                final_score += score
            else:
                stack.append((score, time))
print(final_score)