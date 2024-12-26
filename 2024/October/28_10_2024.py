from typing import List


# My Solution
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak = 0
        unique_numbers = set(nums)
        for start_number in nums:
            current_streak = 0
            current = start_number
            while current in unique_numbers:
                current_streak += 1
                if current * current > 10**5:
                    break
                current *= current
            longest_streak = max(longest_streak, current_streak)
        return longest_streak if longest_streak >= 2 else -1


# Best / Most Optimal Solution
class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        num_set = set(nums)
        max_length = 0
        for num in nums:
            length = 0
            current = num
            while current in num_set:
                length += 1
                current = current**2
            if length > 1:
                max_length = max(max_length, length)
        return max_length if max_length > 1 else -1
