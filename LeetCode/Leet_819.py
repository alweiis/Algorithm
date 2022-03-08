class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = ''
        for c in paragraph:
            if c.isalpha() or c.isspace():
                words += c.lower()
            elif c == ',':
                words += ' '
        words = Counter(words.split())
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for k, v in words:
            if k not in banned:
                return k