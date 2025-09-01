def solution(L, x):
    for idx, val in enumerate(L):
        if x <= val:
            L.insert(idx, x)
            break
    else:
        L.append(x)
    return L