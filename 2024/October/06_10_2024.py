# My Solution
class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1_words = s1.split(" ")
        s2_words = s2.split(" ")
        start, ends1, ends2 = 0, len(s1_words) - 1, len(s2_words) - 1
        if len(s1_words) > len(s2_words):
            return self.areSentencesSimilar(s2, s1)
        while start < len(s1_words) and s1_words[start] == s2_words[start]:
            start += 1
        while ends1 >= 0 and s1_words[ends1] == s2_words[ends2]:
            ends1 -= 1
            ends2 -= 1
        return ends1 < start

# Best / Most Optimal Solution
class Solution2:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        i, j = 0, 0
        n, m = len(words1), len(words2)
        while i < n and i < m and words1[i] == words2[i]:
            i += 1
        while j < (n - i) and j < (m - i) and words1[n - j - 1] == words2[m - j - 1]:
            j += 1
        return i + j == n or i + j == m
