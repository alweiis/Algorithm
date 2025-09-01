def solution(numbers):
    chk_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in numbers:
        chk_arr.remove(num)
    answer = sum(chk_arr)
    return answer