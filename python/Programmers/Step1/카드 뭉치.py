from collections import deque

def solution(cards1, cards2, goal):
    deq1, deq2 = deque(cards1), deque(cards2)
    flag = True
    for target in goal:
        if deq1 and target == deq1[0]:
            deq1.popleft()
            continue
        if deq2 and target == deq2[0]:
            deq2.popleft()
            continue
        flag = False
        break
    answer = "Yes" if flag else "No"
    return answer