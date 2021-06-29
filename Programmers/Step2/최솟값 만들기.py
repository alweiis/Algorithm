def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for idx in range(len(A)):
        answer += A[idx] * B[idx]
    return answer