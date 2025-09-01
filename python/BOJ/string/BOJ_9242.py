number_code = [input() for _ in range(5)]
code_dict = {
    '0': ['*****', '*   *', '*****'],
    '1': ['     ', '     ', '*****'],
    '2': ['* ***', '* * *', '*** *'],
    '3': ['* * *', '* * *', '*****'],
    '4': ['***  ', '  *  ', '*****'],
    '5': ['*** *', '* * *', '* ***'],
    '6': ['*****', '* * *', '* ***'],
    '7': ['*    ', '*    ', '*****'],
    '8': ['*****', '* * *', '*****'],
    '9': ['*** *', '* * *', '*****']
}
arr = []
for j in range(len(number_code[0])):
    tmp = ''
    if j % 4 == 3:
        continue
    for i in range(5):
        tmp += number_code[i][j]
    arr.append(tmp)

result = ''
for i in range(0, len(arr), 3):
    corrected = False
    for num, code in code_dict.items():
        if code == arr[i:i+3]:
            corrected = True
            result += num
    if not corrected:
        print('BOOM!!')
        exit()
print('BEER!!' if int(result) % 6 == 0 else 'BOOM!!')