def recursive(x):
    if x == 1:
        return 1
    elif x < 1:
        return 0
    else:
        return recursive(x - 1) + recursive(x - 2)