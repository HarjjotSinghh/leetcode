from typing import List


# My Solution
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        for i in range(len(nums)):
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask
        return ans


# Best / Most Optimal Solution
class Solution2:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [(1 << maximumBit) - 1]
        for n in nums:
            ans.append(ans[-1] ^ n)
        return ans[len(ans) - 1 : 0 : -1]
