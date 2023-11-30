def solution(data, ext, val_ext, sort_by):
    check = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = []
    for d in data:
        if d[check[ext]] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x: x[check[sort_by]])
    return answer