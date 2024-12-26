import sys
import json
from typing import List

# My Solution
class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        indices_stack = []
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)
        max_width = 0
        for j in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                indices_stack.pop()
        return max_width

# Best / Most Optimal Solution
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                res = max(res, j - stack.pop())
        return res
def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines)
    results = []
    for i in range(num_test_cases):
        nums = json.loads(lines[i])
        result = Solution().maxWidthRamp(nums)
        results.append(str(result))
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    main()
    exit(0)
