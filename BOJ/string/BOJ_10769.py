message = input()
happy_emoji = message.count(':-)')
sad_emoji = message.count(':-(')
if happy_emoji == sad_emoji == 0:
    print('none')
elif happy_emoji > sad_emoji:
    print('happy')
elif happy_emoji < sad_emoji:
    print('sad')
else:
    print('unsure')
