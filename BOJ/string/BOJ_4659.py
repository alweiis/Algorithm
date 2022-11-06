while True:
    password = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    available = ['ee', 'oo']
    if password == 'end':
        break
    quality, vowel = True, False
    for c in password:
        if c in vowels:
            vowel = True
    if not vowel:
        quality = False
    if quality and len(password) >= 3:
        for i in range(len(password)-2):
            if password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels:
                quality = False
            if password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels:
                quality = False
    if quality:
        for i in range(len(password)-1):
            if password[i] == password[i+1] and password[i:i+2] not in available:
                quality = False
    if quality:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')