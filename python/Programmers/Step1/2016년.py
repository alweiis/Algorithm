def solution(a, b):
    cal = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = 0
    for i in range(1, a):
        day += cal[i]
    day += b
    return week[day % 7]