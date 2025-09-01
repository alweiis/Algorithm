import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    lower_c, upper_c, num_c, space_c = 0, 0, 0, 0
    for c in line:
        if c.isdigit():
            num_c += 1
        elif c.isspace():
            space_c += 1
        elif c.isupper():
            upper_c += 1
        elif c.islower():
            lower_c += 1
    print(lower_c, upper_c, num_c, space_c)