def check_trophy():
    count = 1
    for i in range(1, n):
        if max(arr[:i]) < arr[i]:
            count += 1
    return count

n = int(input())
arr = [int(input()) for _ in range(n)]
print(check_trophy())
arr.reverse()
print(check_trophy())