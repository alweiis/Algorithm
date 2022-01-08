N, K = map(int, input().split())
man_array, woman_array = [0] * 7, [0] * 7
room_cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    if S:   # 성별이 '남'
        man_array[Y] += 1
    else:   # 성별이 '여'
        woman_array[Y] += 1
for idx, val in enumerate(man_array, start=1):
    while val > 0:
        val -= K
        room_cnt += 1
for idx, val in enumerate(woman_array, start=1):
    while val > 0:
        val -= K
        room_cnt += 1
print(room_cnt)