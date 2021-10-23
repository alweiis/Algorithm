from sys import stdin
n = 0
trees = dict()
while True:
    tree = stdin.readline().rstrip('\n')
    if not tree:
        break
    trees[tree] = trees.get(tree, 0) + 1
    n += 1

result = sorted(trees.items())
for tree, cnt in result:
    print('{0} {1:0.4f}'.format(tree, cnt * 100 / n))