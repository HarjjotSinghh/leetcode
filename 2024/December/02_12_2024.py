# My Solution
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words, 1):
            if word[: len(searchWord)] == searchWord:
                return i
        return -1


# Best / Most Optimal Solution
class Solution2:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next(
            (i for i, w in enumerate(sentence.split(), 1) if w.startswith(searchWord)),
            -1,
        )
