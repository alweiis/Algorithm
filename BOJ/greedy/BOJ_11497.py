from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    trees = sorted(map(int, input().split()), reverse=True)
    q = deque([trees[0]] + [0] * (n-1))
    del trees[0]
    left, right = 1, n-1
    flag = True
    while left < right:
        for tree in trees:
            if flag:
                q[left] = tree
                flag = False
                left += 1
            else:
                q[right] = tree
                flag = True
                right -= 1
    answer = 0
    for _ in range(n):
        answer = max(answer, abs(q[0] - q[1]))
        q.rotate(-1)
    print(answer)