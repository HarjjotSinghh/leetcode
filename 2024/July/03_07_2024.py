from typing import List
from collections import heapq

# My Soution 
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0
        smallest_four = sorted(heapq.nsmallest(4, nums))
        largest_four = sorted(heapq.nlargest(4, nums))
        min_diff = float("inf")
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])
        return min_diff

# Best / Most Optimal Solution
def minDifference(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    return min(
        nums[-1] - nums[3],
        nums[-2] - nums[2],
        nums[-3] - nums[1],
        nums[-4] - nums[0]
    )
f = open('user.out','w')
for i in map(loads,stdin):
    f.write(f'{minDifference(i)}\n') 
f.flush()
exit(0)
