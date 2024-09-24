
# My Solution
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans

# Best / Most Optimal Solution
class Solution2:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        currLen=1
        currCopy=1
        currOperations=1
        while currLen<n:
            if n%currLen == 0 and currLen!=currCopy:
                currCopy=currLen
            else:
                currLen+=currCopy
            currOperations+=1
        return currOperations