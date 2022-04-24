from itertools import permutations
n = int(input())
k = int(input())
card_lst = [input() for _ in range(n)]
arr = list(permutations(card_lst, k))
card_set = {"".join(nums) for nums in arr}

print(len(card_set))
