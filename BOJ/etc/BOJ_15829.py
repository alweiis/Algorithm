from string import ascii_lowercase
length = int(input())
strings = input()
alphabet_dic = {c: idx for idx, c in enumerate(ascii_lowercase, start=1)}
hash_code = 0
a = [alphabet_dic[c] for c in strings]
for i in range(length):
    hash_code += a[i] * (31 ** i)
print(hash_code % 1234567891)