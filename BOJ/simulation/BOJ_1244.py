n = int(input())    # 스위치 수
switch = list(map(int, input().split()))
m = int(input())    # 학생 수
def switch_change(arr, x):
    if arr[x] == 1:
        arr[x] = 0
    else:
        arr[x] = 1
for _ in range(m):
    x, num = map(int, input().split())
    if x == 1:      # 남자
        for i in range(num-1, n, num):
            switch_change(switch, i)
    else:           # 여자
        switch_change(switch, num-1)
        left, right = num-2, num
        while 0 <= left and right < n:
            if switch[left] == switch[right]:
                switch_change(switch, left)
                switch_change(switch, right)
                left -= 1
                right += 1
            else:
                break
for i in range(1, n+1):
    print(switch[i-1], end=' ')
    if i % 20 == 0:
        print()