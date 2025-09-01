def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    for s in skill_trees:
        sp, cp = 0, 0
        possible = True
        while sp != len(skill) and cp != len(s):
            if s[cp] not in skill_set:
                cp += 1
            else:
                if skill[sp] == s[cp]:
                    sp += 1
                    cp += 1
                else:
                    possible = False
                    break
        if possible:
            answer += 1
    return answer
