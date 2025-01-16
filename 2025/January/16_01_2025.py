from typing import List


# My Solution
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        if len2 % 2:
            for num in nums1:
                xor1 ^= num
        if len1 % 2:
            for num in nums2:
                xor2 ^= num
        return xor1 ^ xor2


# Best / Most Optimal Solution
class Solution2:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        if n2 % 2 == 1:
            for i in range(n1):
                ans = ans ^ nums1[i]
        if n1 % 2 == 1:
            for i in range(n2):
                ans = ans ^ nums2[i]
        return ans
