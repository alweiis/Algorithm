def solution(prices):
    answer = []
    arr_length = len(prices)
    max_second = arr_length - 1
    for i in range(arr_length):
        for j in range(i+1, arr_length):
            if prices[i] > prices[j]:
                interval_second = j - i
                answer.append(interval_second)
                break
        else:
            answer.append(max_second)
        max_second -= 1
    return answer