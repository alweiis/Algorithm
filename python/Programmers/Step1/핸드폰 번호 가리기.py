def solution(phone_number):
    number_len = len(phone_number) - 4
    result = '*' * number_len + phone_number[-4:]
    return result
