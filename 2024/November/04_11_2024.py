# My Solution
class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        pos = 0
        while pos < len(word):
            consecutive_count = 0
            current_char = word[pos]
            while (
                pos < len(word) and consecutive_count < 9 and word[pos] == current_char
            ):
                consecutive_count += 1
                pos += 1
            comp.append(str(consecutive_count))
            comp.append(current_char)
        return "".join(comp)


# Best / Most Optimal Solution
class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        comp = []
        current_char = word[0]
        count = 1
        for c in word[1:]:
            if c == current_char:
                if count == 9:
                    comp.append("9")
                    comp.append(current_char)
                    count = 1
                else:
                    count += 1
            else:
                comp.append(str(count))
                comp.append(current_char)
                current_char = c
                count = 1
        comp.append(str(count))
        comp.append(current_char)
        return "".join(comp)
