from collections import deque
n = int(input())
cards = deque(map(int, input().split()))
x = cards.index(max(cards))
cards.rotate(-x)
gold = 0
while len(cards) >= 2:
    num1 = cards.popleft()
    num2 = cards.popleft()
    gold += num1 + num2
    cards.appendleft(num1)
print(cards[0] if n == 1 else gold)