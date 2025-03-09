from typing import List

# My Solution
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        length = len(colors)
        result = 0
        left = 0
        right = 1
        while right < length:
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue
            right += 1
            if right - left < k:
                continue
            result += 1
            left += 1
        return result

# Best / Most Optimal Solution
class Solution2:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = []
        n = len(colors)
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                l.append(i)
        if colors[n - 1] == colors[0]:
            l.append(n - 1)
        if len(l) == 0:
            return n
        l.append(l[0] + n)
        res = 0
        for i in range(len(l) - 1):
            res += max(0, l[i + 1] - l[i] - k + 1)
        return res
