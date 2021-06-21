class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for ele in S:
        if ele.isalpha():
            answer.join(ele)
        else:
            if opStack.size() == 0:
                opStack.push(ele)
            if ele == '(':
                opStack.push(ele)
            elif ele == ')':
                while not opStack.peek() == '(':
                    answer.join(opStack.pop())
            else:
                if prec.get(ele) >= prec.get(opStack.peek()):
                    answer.join(opStack.pop())
                else:
                    opStack.push(ele)
    while not opStack.isEmpty():
        answer.join(opStack.pop())
    return answer