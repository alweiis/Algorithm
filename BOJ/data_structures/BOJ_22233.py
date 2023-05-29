from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
memo_keyword = {input().rstrip() for _ in range(n)}
for _ in range(m):
    used_words = set(input().rstrip().split(','))
    for word in used_words:
        memo_keyword.discard(word)
    print(len(memo_keyword))