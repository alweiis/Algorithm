def solution(num):
    if num == 1 or num == 2:
        return 1
    bottom_up = [0] * (num + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, num + 1):
        bottom_up[i] = (bottom_up[i-1] + bottom_up[i-2]) % 1234567
    return bottom_up[-1]