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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    print(tokens)
    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            if not opStack.isEmpty():
                stack = opStack.peek()
                while prec[token] <= prec[stack]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(token)
            else:
                opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            opStack.push(token)
        else:
            val1 = opStack.pop()
            val2 = opStack.pop()
            calc = 0
            if token == '*':
                calc = val2 * val1
            elif token == '/':
                calc = val2 / val1
            elif token == '+':
                calc = val2 + val1
            elif token == '-':
                calc = val2 - val1
            opStack.push(calc)
    result = opStack.pop()
    return result


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
