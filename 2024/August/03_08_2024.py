from typing import List
from sys import stdin
from json import loads

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        mp = {}
        for num in arr:
            mp[num] = mp.get(num, 0) + 1
        for num in target:
            if num not in mp:
                return False
            mp[num] -= 1
            if mp[num] == 0:
                del mp[num]
        return len(mp) == 0

# Best / Most Optimal Solution
class Solution2:
    with open("user.out", "w") as f:
        for target, arr in zip(map(loads, stdin), map(loads, stdin)):
            f1 = {}
            f2 = {}
            for num in target:
                if num not in f1:
                    f1[num] = 0
                f1[num] += 1
            for num in arr:
                if num not in f2:
                    f2[num] = 0
                f2[num] += 1
            print(["true", "false"][f1 != f2], file=f)
    exit()
