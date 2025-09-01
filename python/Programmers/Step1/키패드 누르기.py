def solution(numbers, hand):
    keypad = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
              '4': (1, 0), '5': (1, 1), '6': (1, 2),
              '7': (2, 0), '8': (2, 1), '9': (2, 2),
              '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    answer = ''
    l, r = '*', '#'
    for n in numbers:
        n = str(n)
        if n in ['1', '4', '7']:
            l = n
            answer += 'L'
        elif n in ['3', '6', '9']:
            r = n
            answer += 'R'
        else:
            l_distance = abs(keypad[n][0] - keypad[l][0]) + abs(keypad[n][1] - keypad[l][1])
            r_distance = abs(keypad[n][0] - keypad[r][0]) + abs(keypad[n][1] - keypad[r][1])
            if l_distance < r_distance:
                l = n
                answer += 'L'
            elif l_distance > r_distance:
                r = n
                answer += 'R'
            else:
                if hand == 'left':
                    l = n
                    answer += 'L'
                elif hand == 'right':
                    r = n
                    answer += 'R'
    return answer