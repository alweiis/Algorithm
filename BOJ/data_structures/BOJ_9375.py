for _ in range(int(input())):
    hanger = {}
    answer = 1
    for _ in range(int(input())):
        clothes, group = input().split()
        if hanger.get(group):
            hanger[group].append(clothes)
        else:
            hanger[group] = [clothes]
    for clothes in hanger.values():
        answer *= len(clothes) + 1
    print(answer - 1)