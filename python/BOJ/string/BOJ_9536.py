n = int(input())
for _ in range(n):
    sound = input().split()
    while True:
        check = input().split()
        if len(check) > 3:
            break
        while check[-1] in sound:
            sound.remove(check[-1])
    print(' '.join(sound))