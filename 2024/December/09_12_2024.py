from typing import List

# My Solution
class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        max_reach = [0] * n
        end = 0
        for start in range(n):
            end = max(end, start)
            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            max_reach[start] = end
        ans = []
        for start, end_query in queries:
            ans.append(end_query <= max_reach[start])
        return ans

# Best / Most Optimal Solution
class Solution2:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        runningSum = 0
        partialSum = []
        oddEven = None
        for num in nums:
            if num % 2 == oddEven:
                runningSum += 1
            oddEven = num % 2
            partialSum.append(runningSum)
        out = []
        for start, end in queries:
            if partialSum[start] == partialSum[end]:
                out.append(True)
            else:
                out.append(False)
        return out
