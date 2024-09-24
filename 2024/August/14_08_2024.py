from typing import List

# My Solution
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)
        low = 0
        high = nums[array_size - 1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count = self._count_pairs_with_max_distance(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
    def _count_pairs_with_max_distance(
        self, nums: List[int], max_distance: int
    ) -> int:
        count = 0
        array_size = len(nums)
        left = 0
        for right in range(array_size):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left
        return count
    
# Best / Most Optimal Solution
class Solution2:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        def func(x):
            count, left, right = 0, 0, 0 
            for right in range(n):
                while nums[right] - nums[left] > x:
                    left += 1 
                count += right-left 
            return count 
        low, high = 0, nums[-1]-nums[0]
        while low <= high:
            mid = (low+high)//2 

            if func(mid) < k:
                low = mid + 1 
            else:
                high = mid - 1 
        return low
    