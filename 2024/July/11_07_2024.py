
# My Solution
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i
        result = []
        curr_index = 0
        direction = 1
        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction
        return "".join(result)
    
# Best / Most Optimal Solution
class Solution2:
    def reverseParentheses(self, s: str) -> str:
        sub = list(s)
        i = len(sub) - 1
        while "(" in sub:
            if sub[i] == "(":
                for j in range(i, len(sub)):
                    if sub[j] == ")":
                        sub[i + 1 : j] = sub[i + 1 : j][::-1]
                        sub.pop(j)
                        sub.pop(i)
                        break
            i -= 1
        return "".join(sub)
