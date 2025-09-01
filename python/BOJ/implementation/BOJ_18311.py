n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = [i for i in range(1, n + 1)]
result.extend(list(reversed(result)))
race = [arr[0]]
for i in range(1, n):
    race.append(race[-1] + arr[i])
for i in range(n - 1, -1, -1):
    race.append(race[-1] + arr[i])
for i in range(2 * n):
    if race[i] > k:
        print(result[i])
        break