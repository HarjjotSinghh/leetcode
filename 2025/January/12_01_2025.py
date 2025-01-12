# My Solution
class Solution:
    def canBeValid(self, s, locked):
        length = len(s)
        if length % 2 == 1:
            return False
        open_brackets = []
        unlocked = []
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        if open_brackets:
            return False
        return True


# Best / Most Optimal Solution
class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False
        brackets = []
        arr = []
        for i in range(n):
            if locked[i] == "0":
                arr.append(i)
            elif s[i] == "(":
                brackets.append(i)
            else:
                if brackets:
                    brackets.pop()
                elif arr:
                    arr.pop()
                else:
                    return False
        while brackets and arr and brackets[-1] < arr[-1]:
            brackets.pop()
            arr.pop()
        if brackets:
            return False
        return True
