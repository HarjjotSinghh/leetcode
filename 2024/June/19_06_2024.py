from typing import List

# My Solution 
class Solution:
    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        count = 0
        for day in bloomDay:
            if day <= mid:
                count += 1
            else:
                count = 0
            if count == k:
                num_of_bouquets += 1
                count = 0
        return num_of_bouquets
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        start = 0
        end = max(bloomDay)
        minDays = -1
        while start <= end:
            mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1
        return minDays
    
# Best / Most Optimal Solution
class Solution2:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(x):
            total = 0
            currcount = 0
            for b in bloomDay:
                if x>=b:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            total += currcount // k
            if total >= m:
                return True
        if m*k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left
