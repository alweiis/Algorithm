nums = [int(input()) for _ in range(10)]
calc = 0
result = 0
for num in nums:
    tmp = calc
    tmp += num
    if tmp >= 100:
        after_sum = abs(100 - tmp)
        before_sum = abs(100 - calc)
        # 수를 더한 후의 절댓값이 더하기 전 절댓값보다 작거나 같은 경우
        if after_sum <= before_sum:
            result = tmp
            break
        else:
            result = calc
            break
    calc = tmp
# 10개의 수를 모두 더해도 100이 안되는 경우
else:
    result = calc
print(result)