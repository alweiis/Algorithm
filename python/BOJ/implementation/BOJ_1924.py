x, y = map(int, input().split())
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_interval, day_interval = x - 1, y - 1
total_day = sum(month[:month_interval]) + day_interval
print(week[total_day % 7])