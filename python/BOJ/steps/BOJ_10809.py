from string import ascii_lowercase

alpha_list = list(ascii_lowercase)

word = input()
for alpha in alpha_list:
    print(word.find(alpha), end=' ')
