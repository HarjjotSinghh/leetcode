from typing import List


# My Solution
class Solution:
    def stringMatching(self, words):
        matching_words = []
        for current_word_index in range(len(words)):
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break
        return matching_words


# Best / Most Optimal Solution
class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        r = " ".join(words)
        s = [i for i in words if r.count(i) > 1]
        return s
