n = int(input())
formula = input()
alphabet = {}
start = 65                      # chr(65) = 'A'
for _ in range(n):
    alphabet[chr(start)] = input()
    start += 1
stack = []
for c in formula:
    if c.isalpha():
        stack.append(alphabet[c])
    else:
        first = stack.pop()     # stack에서 첫 번째로 뽑은 값
        second = stack.pop()    # stack에서 두 번째로 뽑은 값
        stack.append(str(eval(second + c + first)))
print(f'{float(stack[0]):0.2f}')