from typing import List

# My Solution
class Solution:
    def minCapability(self, nums, k):
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0
            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2
                else:
                    index += 1
            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1
        return min_reward

# Best / Most Optimal Solution
class Solution2:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(cap):
            count = taken = 0
            for x in nums:
                if taken:
                    taken = False
                elif x <= cap:
                    count += 1
                    taken = True
            return count >= k
        items = list(sorted(set(nums)))
        l, r = 0, len(items) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if check(items[mid]):
                r = mid
            else:
                l = mid + 1
        return items[l] if check(items[l]) else items[r]
