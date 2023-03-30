def solution(name, yearning, photo):
    data = dict(zip(name, yearning))
    answer = []
    for p in photo:
        result = 0
        for key in p:
            if type(data.get(key)) == int:
                result += data.get(key)
        answer.append(result)
    return answer