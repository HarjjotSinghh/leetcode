# My Solution
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        previous_index = 0
        for current_index in range(len(pattern) + 1):
            result.append(str(1 + current_index))
            if current_index == len(pattern) or pattern[current_index] == "I":
                result[previous_index:] = reversed(result[previous_index:])
                previous_index = current_index + 1
        return "".join(result)


# Best / Most Optimal Solution
class Solution2:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [i for i in range(1, n + 2)]
        i = 0
        while i < n:
            t = i
            while t < n and pattern[t] == "D":
                t += 1
            res[i : t + 1] = reversed(res[i : t + 1])
            if t != i:
                i = t - 1
            i += 1
        return "".join(map(str, res))
