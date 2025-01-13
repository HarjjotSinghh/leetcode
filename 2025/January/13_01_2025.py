# My Solution
class Solution:
    def minimumLength(self, s: str) -> int:
        char_frequency = [0] * 26
        total_length = 0
        for current_char in s:
            char_frequency[ord(current_char) - ord("a")] += 1
        for frequency in char_frequency:
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                total_length += 2
            else:
                total_length += 1
        return total_length


# Best / Most Optimal Solution
class Solution2:
    def minimumLength(self, s: str) -> int:
        s_set = {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        }
        ans = 0
        for ch in s_set:
            count = s.count(ch)
            if count & 1:
                ans += 1
            elif count != 0:
                ans += 2
        return ans
