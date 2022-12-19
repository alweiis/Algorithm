n, *arr = input().split()
while len(arr) < int(n):
    data = input().split()
    arr.extend(data)
answer = [int(element[::-1]) for element in arr]
answer.sort()
print(*answer, sep='\n')