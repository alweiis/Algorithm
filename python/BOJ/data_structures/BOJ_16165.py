from collections import defaultdict
n, m = map(int, input().split())
group = defaultdict(list)
for _ in range(n):
    team_name = input()
    member_count = int(input())
    for _ in range(member_count):
        name = input()
        group[team_name].append(name)
for _ in range(m):
    name = input()
    kind = int(input())
    if kind == 0:
        for member_name in sorted(group[name]):
            print(member_name)
    elif kind == 1:
        for team_name, member_name in group.items():
            if name in member_name:
                print(team_name)