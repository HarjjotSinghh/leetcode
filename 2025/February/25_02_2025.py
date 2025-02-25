from typing import List


# My Solution
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0
        odd_count = 0
        even_count = 1
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1
            count %= MOD
        return count


# Best / Most Optimal Solution
class Solution2:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cumSum = odd = even = 0
        for num in arr:
            cumSum += num
            if cumSum % 2:
                odd += 1
            else:
                even += 1
        return odd * (even + 1) % (pow(10, 9) + 7)
