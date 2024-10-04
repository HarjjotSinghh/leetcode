from collections import Counter
from typing import List
from sys import stdin
from json import loads

# My Solution
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)
        if total_skill % (n // 2) != 0:
            return -1
        target_skill = total_skill // (n // 2)
        skill_map = Counter(skill)
        total_chemistry = 0
        for curr_skill, curr_freq in skill_map.items():
            partner_skill = target_skill - curr_skill
            if (
                partner_skill not in skill_map
                or curr_freq != skill_map[partner_skill]
            ):
                return -1
            total_chemistry += curr_skill * partner_skill * curr_freq
        return total_chemistry // 2

# Best / Most Optimal Solution
class Solution2:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_ = sum(skill)
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        if sum_ % (n//2) != 0:
            return -1
        skill.sort()
        score = skill[0] + skill[-1]
        pairs = []
        result = 0
        for i in range(n // 2):
            l, r = skill[i], skill[n - 1 - i]
            if l + r != score:
                return -1
            result += l * r
        return result
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().dividePlayers(nums),file=f)
exit(0)
