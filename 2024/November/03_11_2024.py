# My Solution
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_string = s + s
        return doubled_string.find(goal) != -1


# Best / Most Optimal Solution
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False
