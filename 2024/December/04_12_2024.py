# My Solution
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if (
                str1[i] == str2[j]
                or chr((ord(str1[i]) - ord("a") + 1) % 26 + ord("a")) == str2[j]
            ):
                j += 1
            i += 1
        return j == len(str2)


# Best / Most Optimal Solution
class Solution2:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) == len(str2):
            for i in range(len(str1)):
                if str2[i] == "a" and str1[i] == "z":
                    continue
                elif str1[i] == str2[i]:
                    continue
                elif ord(str2[i]) - ord(str1[i]) != 1:
                    return False
            return True
        l = []
        if len(str2) > len(str1):
            return False
        for i in str2:
            if i not in str1:
                l.append(i)
        c = 0
        for i in l:
            if chr(ord(i) - 1) in str1:
                c += 1
            if i == "a" and "z" in str1:
                c += 1
        return c == len(l)
