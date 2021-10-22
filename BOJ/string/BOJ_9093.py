for _ in range(int(input())):
    st = input().split(' ')
    for word in st:
        print(word[::-1], end=' ')
    print()