class Solution:
    def isPalindrome(self, s: str) -> bool:
        chk = ''
        for c in s:
            if c.isalpha() or c.isnumeric():
                chk += c
        chk = chk.lower()
        if chk == chk[::-1]:
            return True
        return False