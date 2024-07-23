from collections import Counter
from typing import List

# My Solution
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
    
# Best / Most Optimal Solution
class Solution2:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        sorted_nums = sorted(nums, key=lambda x: (freq_dict[x], -x))
        return sorted_nums
