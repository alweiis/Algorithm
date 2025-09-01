vowel = 'aiyeou'
consonant = 'bkxznhdcwgpvjqtsrlmf'

# 미리 변환 테이블을 만들어둠
vowel_map = {vowel[i]: vowel[(i + 3) % 6] for i in range(6)}
consonant_map = {consonant[i]: consonant[(i + 10) % 20] for i in range(20)}

# 대문자 변환도 미리 준비
vowel_map.update({k.upper(): v.upper() for k, v in vowel_map.items()})
consonant_map.update({k.upper(): v.upper() for k, v in consonant_map.items()})

# 변환 로직
while True:
    try:
        rot13 = input()
        origin = []
        for c in rot13:
            if c in vowel_map:
                origin.append(vowel_map[c])
            elif c in consonant_map:
                origin.append(consonant_map[c])
            else:
                origin.append(c)
        print(''.join(origin))
    except:
        break