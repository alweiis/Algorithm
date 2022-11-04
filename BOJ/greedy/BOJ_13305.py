import math

n = int(input())
distance = list(map(int, input().split()))
gas_station = list(map(int, input().split()))
gas = math.inf
answer = 0
for i in range(n-1):
    if gas_station[i] <= gas:
        answer += gas_station[i] * distance[i]
        gas = gas_station[i]
    else:
        answer += gas * distance[i]
print(answer)