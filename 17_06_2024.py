from math import sqrt

# My Solution
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i * i for i in range(int(sqrt(c) + 1))]
        left = 0
        right = len(nums) - 1
        while left <= right:
            sqrSum = nums[left] + nums[right]
            if sqrSum == c:
                return True
            if sqrSum > c:
                right -= 1
            else:
                left += 1
        return False

# Best / Most Optimal Solution
class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if count % 2 and i % 4 == 3:
                    return False
            i += 1
        return c % 4 != 3
