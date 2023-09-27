from sys import stdin
input = stdin.readline

def next_permutation(s):
    k = -1
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            k = i
    if k == -1:
        return s

    for i in range(len(s)-1, -1, -1):
        if s[k] < s[i]:
            m = i
            break

    s[k], s[m] = s[m], s[k]
    result = s[:k + 1]
    result.extend(list(reversed(s[k + 1:])))
    return result

t = int(input())
words = [input().rstrip() for _ in range(t)]
for word in words:
    answer = next_permutation(list(word))
    print(''.join(answer))