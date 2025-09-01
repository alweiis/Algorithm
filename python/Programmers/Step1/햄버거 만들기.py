def solution(ingredient):
    hamburger = [1, 2, 3, 1]
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == hamburger:
            answer += 1
            del stack[-4:]
    return answer