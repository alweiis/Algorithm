import sys
input = sys.stdin.readline
n, m = map(int, input().split())
notepad = {}
for _ in range(n):
    address, password = input().split()
    notepad[address] = password
for _ in range(m):
    address = input().rstrip()
    print(notepad[address])