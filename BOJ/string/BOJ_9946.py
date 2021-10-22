num = 1
while True:
    fst_word, scn_word = input(), input()
    if fst_word == scn_word == 'END':
        break
    fst_word = ''.join(sorted(fst_word))
    scn_word = ''.join(sorted(scn_word))
    print('Case {}: {}'.format(num, 'same' if fst_word == scn_word else 'different'))
    num += 1
