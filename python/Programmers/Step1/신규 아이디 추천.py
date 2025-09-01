import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^a-z0-9-_.]", "", answer)
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer
