t = int(input())
for tc in range(1, t + 1):
    arr = sorted(map(int, input().split()))
    result = round(sum(arr[1:9]) / 8)
    print(f'#{tc} {result}')