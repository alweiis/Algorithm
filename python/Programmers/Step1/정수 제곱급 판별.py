import math

def solution(n):
    num = math.sqrt(n)
    if num == int(num) :
        return pow(num+1, 2)
    return -1