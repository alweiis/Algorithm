import string
import sys
word = sys.stdin.readline().rstrip()
for letter in string.ascii_lowercase:
    print(word.count(letter), end=' ')