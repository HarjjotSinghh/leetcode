from typing import List
from bisect import bisect_left


# My Solution
class Solution:
    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]
        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])
            if index == len(lis):
                lis.append(v[i])
            else:
                lis[index] = v[i]
            lis_len[i] = len(lis)
        return lis_len

    def lowerBound(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        lis_length = self.getLongestIncreasingSubsequenceLength(nums)
        nums.reverse()
        lds_length = self.getLongestIncreasingSubsequenceLength(nums)
        lds_length.reverse()
        min_removals = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(min_removals, N - lis_length[i] - lds_length[i] + 1)
        return min_removals


# Best / Most Optimal Solution
class Solution2:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def getLis(arr):
            res = [0] * n
            stack = []
            for i in range(n):
                if stack and stack[-1] >= arr[i]:
                    j = bisect_left(stack, arr[i])
                    stack[j] = arr[i]
                    res[i] = j + 1
                else:
                    stack.append(arr[i])
                    res[i] = len(stack)
            return res

        left, right = getLis(nums), getLis(nums[::-1])[::-1]
        ans = float("inf")
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                ans = min(ans, n - (left[i] + right[i] - 1))
        return ans
