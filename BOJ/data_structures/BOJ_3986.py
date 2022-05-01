n = int(input())
good_word = 0
for _ in range(n):
    word = input()
    stack = []
    for c in word:
        stack.append(c)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack = stack[0:-2]
    if not stack:
        good_word += 1
print(good_word)