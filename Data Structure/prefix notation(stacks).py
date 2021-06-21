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
    for c in S:
        if c.isalpha():
            answer += c
        else:
            if c == '(':
                opStack.push(c)
            elif c == ')':
                while not opStack.peek() == '(':
                    answer += opStack.pop()
                opStack.pop()
            elif not opStack.isEmpty():
                s = opStack.peek()
                while prec[c] <= prec[s]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
                opStack.push(c)
            else:
                opStack.push(c)

    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer
