def solution(arr, divisor):
    answer = sorted(list(arr[i] for i in range(len(arr)) if arr[i] % divisor == 0))
    if len(answer) == 0:
        answer = [-1]
    return answer