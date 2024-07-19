from typing import List

# My Solution
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def isOdd(num: int):
            return num % 2 != 0
        for i in range(len(arr)-2):
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True
        return False

# Best / Most Optimal Solution
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num % 2 == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
