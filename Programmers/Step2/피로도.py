from itertools import permutations
def solution(k, dungeons):
    permutation = list(permutations(dungeons))
    answer = 0
    for arr in permutation:
        energy = k
        count = 0
        for a, b in arr:
            if energy >= a:
                energy -= b
                count += 1
        answer = max(answer, count)
    return answer