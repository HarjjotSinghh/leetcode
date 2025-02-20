from typing import List


# My Solution
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)


# Best / Most Optimal Solution
class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i, num in enumerate(nums):
            ans += str(abs(int(num[i]) - 1))
        return ans
