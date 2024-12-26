from typing import List


# My Solution
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            if i in spaces:
                res += f" {s[i]}"
            else:
                res += s[i]
        return res


# Best / Most Optimal Solution
class Solution2:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        result = [None] * (len(s) + len(spaces))
        space_index = 0
        string_index = 0
        for char_index in range(len(s)):
            if space_index < len(spaces) and char_index == spaces[space_index]:
                result[string_index] = " "
                string_index += 1
                space_index += 1
            result[string_index] = s[char_index]
            string_index += 1
        return "".join(result[:string_index])
