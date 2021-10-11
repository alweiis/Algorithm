scores = sorted([(int(input()), idx + 1) for idx in range(8)])
total_score = 0
score_idx = []
for i in range(-1, -6, -1):
    score, index = scores[i]
    total_score += score
    score_idx.append(index)
score_idx.sort()
print(total_score)
print(' '.join(map(str, score_idx)))