# My Solution
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        max_count = [0]
        self.backtrack(s, 0, seen, 0, max_count)
        return max_count[0]

    def backtrack(
        self, s: str, start: int, seen: set, count: int, max_count: list
    ) -> None:
        if count + (len(s) - start) <= max_count[0]:
            return
        if start == len(s):
            max_count[0] = max(max_count[0], count)
            return
        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                self.backtrack(s, end, seen, count + 1, max_count)
                seen.remove(sub_string)
        return


# Best / Most Optimal Solution
class Solution2:
    def backtrack(self, s, index, count, s_set):
        ans = 0
        if len(s) - index + count <= self.ans:
            return
        if index >= len(s):
            self.ans = max(self.ans, count)
            return
        for i in range(index, len(s)):
            sub_s = s[index : i + 1]
            if sub_s not in s_set:
                s_set.add(sub_s)
                self.backtrack(s, i + 1, count + 1, s_set)
                s_set.remove(sub_s)

    def maxUniqueSplit(self, s: str) -> int:
        s_set = set()
        self.ans = 0
        self.backtrack(s, 0, 0, s_set)
        return self.ans
