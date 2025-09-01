from collections import defaultdict
s, p = map(int, input().split())
strings = input()
a, c, g, t = map(int, input().split())
password = defaultdict(int)
answer = 0
def check_password():
    global answer
    if password['A'] >= a and password['C'] >= c and password['G'] >= g and password['T'] >= t:
        answer += 1

for i in range(p):
    password[strings[i]] += 1
check_password()

for i in range(p, s):
    password[strings[i]] += 1
    password[strings[i-p]] -= 1
    check_password()
print(answer)