def solution(babbling):
    possible_word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        if word in possible_word:
            answer += 1
        elif check_word(word, possible_word):
            answer += 1
    return answer

def check_word(temp, check_list):
    stack = []
    while temp:
        if temp[:2] in check_list:
            if stack and stack[-1] == temp[:2]:
                return False
            stack.append(temp[:2])
            temp = temp[2:]
        elif temp[:3] in check_list:
            if stack and stack[-1] == temp[:3]:
                return False
            stack.append(temp[:3])
            temp = temp[3:]
        else:
            return False
    return True