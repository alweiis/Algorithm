hour, minute = map(int, input().split())
cooking_time = int(input())
chk_hour, result_minute = divmod(minute + cooking_time, 60)
result_hour = (hour + chk_hour) % 24
print(result_hour, result_minute)