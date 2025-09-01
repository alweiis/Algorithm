from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    needs = {}
    sales = defaultdict(int)
    for name, quantity in zip(want, number):
        needs[name] = quantity
    for product in discount[0:10]:
        sales[product] += 1
    if needs == sales:
        answer += 1
    for i in range(len(discount)-10):
        sales[discount[i]] -= 1
        if sales[discount[i]] == 0:
            sales.pop(discount[i])
        sales[discount[i+10]] += 1
        if needs == sales:
            answer += 1
    return answer