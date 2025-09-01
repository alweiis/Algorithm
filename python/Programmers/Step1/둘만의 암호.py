from string import ascii_lowercase
from collections import deque

def solution(s, skip, index):
    alphabet = set(ascii_lowercase)
    for c in skip:
        alphabet.remove(c)
    deq = deque(sorted(alphabet))
    answer = []
    for c in s:
        while c != deq[0]:
            deq.rotate(-1)
        deq.rotate(-index)
        answer.append(deq[0])
    return ''.join(answer)