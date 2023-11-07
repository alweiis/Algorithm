def solution(numbers):
    answer = [-1]
    stack = [numbers[-1]]
    for i in range(len(numbers)-2, -1, -1):
        while stack:
            if numbers[i] < stack[-1]:
                answer.append(stack[-1])
                stack.append(numbers[i])
                break
            else:
                stack.pop()
        else:
            answer.append(-1)
            stack.append(numbers[i])
    answer = answer[::-1]
    return answer