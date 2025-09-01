def solution(clothes):
    hash_map = {}
    answer = 1
    for val, key in clothes:
        if key in hash_map:
            hash_map[key].append(val)
        else:
            hash_map[key] = [val]
    for val in hash_map.values():
        answer *= len(val) + 1
    return answer - 1