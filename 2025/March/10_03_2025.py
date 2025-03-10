from collections import defaultdict

# My Solution
class Solution:
    def _isVowel(self, c: str) -> bool:
        return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"
    def countOfSubstrings(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = end = 0
        vowel_count = {}
        consonant_count = 0
        next_consonant = [0] * len(
            word
        )
        next_consonant_index = len(word)
        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i
        while end < len(word):
            new_letter = word[end]
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1
            while (
                consonant_count > k
            ):
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1
            while (
                start < len(word)
                and len(vowel_count) == 5
                and consonant_count == k
            ):
                num_valid_substrings += next_consonant[end] - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1
            end += 1
        return num_valid_substrings

# Best / Most Optimal Solution
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0
        vowels = set('aeiou')
        n = len(word)
        freq = defaultdict(int)
        lo, hi, cnt = 0, 0, 0
        for c in word:
            if c in vowels:
                freq[c] += 1
            else:
                cnt += 1
            while cnt > k:
                if word[hi] in vowels:
                    freq[word[hi]] -= 1
                    if freq[word[hi]] == 0:
                        del freq[word[hi]]
                else:
                    cnt -= 1
                hi += 1
                lo = hi
            while cnt == k and hi < n:
                if word[hi] in vowels and freq[word[hi]] > 1:
                    freq[word[hi]] -= 1
                    if freq[word[hi]] == 0:
                        del freq[word[hi]]
                    hi += 1
                else:
                    break
            if cnt == k and len(freq) == 5:
                res += hi - lo + 1
        return res
