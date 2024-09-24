from typing import List
import json
import sys

# My Solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = current_streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans = current_streak = 0
            if max_val == num:
                current_streak += 1
            else:
                current_streak = 0
            ans = max(ans, current_streak)
        return ans

# Best / Most Optimal Solution
class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        max_len = 1
        current_len = 1
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_len = 1
                current_len = 1
            elif nums[i] == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        return max_len
def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines)
    results = []
    for i in range(num_test_cases):
        nums = json.loads(lines[i])
        
        result = Solution().longestSubarray(nums)
        results.append(str(result))
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    main()
    exit(0)
