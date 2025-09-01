while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        word = input()
        arr.append((word.lower(), word))
    arr.sort(key= lambda x:x[0])
    print(arr[0][1])