import sys
input = sys.stdin.readline

S, E, Q = input().rstrip().split()
S = int(''.join(S.split(':')))
E = int(''.join(E.split(':')))
Q = int(''.join(Q.split(':')))
enter_set, exit_set = set(), set()
while True:
    try:
        time, name = input().rstrip().split()
        time = int(''.join(time.split(':')))
        if time <= S:
            enter_set.add(name)
        elif E <= time <= Q:
            exit_set.add(name)
    except ValueError:
        break
print(len(enter_set & exit_set))