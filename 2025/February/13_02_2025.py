from typing import List
import heapq


# My Solution
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        num_operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            num_operations += 1
        return num_operations


# Best / Most Optimal Solution
class Solution2:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ret = 0
        i = 0
        temp = []
        j = 0
        size = 0
        while (n - i + size - j) >= 2:
            if i < n:
                first = nums[i]
                if j < size and temp[j] < first:
                    first = temp[j]
                    j += 1
                else:
                    i += 1
            else:
                first = temp[j]
                j += 1
            if first >= k:
                break
            if i < n:
                second = nums[i]
                if j < size and temp[j] < second:
                    second = temp[j]
                    j += 1
                else:
                    i += 1
            else:
                second = temp[j]
                j += 1
            new = (min(first, second) * 2) + max(first, second)
            size += 1
            ret += 1
            temp.append(new)
        return ret
