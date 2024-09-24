from typing import List
from json import loads
from sys import stdin

# My Solution ☠️
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

# Best / Most Optimal Solution
class Solution2:
    def __init__(self):
        f = open('user.out', 'w')
        for nums in map(loads, stdin):
            print(str(sorted(nums)).replace(' ',''), file=f)
        exit(0)
