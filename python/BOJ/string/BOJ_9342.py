import re
p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    word = input()
    result = p.match(word)
    if result is None:
        print('Good')
    else:
        print('Infected!')