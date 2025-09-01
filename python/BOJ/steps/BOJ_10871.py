N, X = map(int, input().split())
A = list(map(int, input().split()))
for index in range(N):
    if A[index] < X:
        print(A[index], end=" ")
