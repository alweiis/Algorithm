def palindrome(x):
    if x == x[::-1]:
        return 0
    left = 0
    right = len(x) - 1
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                tmp = x[:right] + x[right + 1:]
                if tmp == tmp[::-1]:
                    return 1
            if left + 1 < right:
                tmp = x[:left] + x[left + 1:]
                if tmp == tmp[::-1]:
                    return 1
            return 2

T = int(input())
words = [input() for _ in range(T)]
for word in words:
    print(palindrome(word))