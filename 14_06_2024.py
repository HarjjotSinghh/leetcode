from typing import List

class Solution:
    # My Solution
    def minIncrementForUnique(self, nums: List[int]) -> int:
        x0, M = min(nums), max(nums)
        n = len(nums)
        freq = [0] * (M + n)
        
        for x in nums:
            freq[x]+=1
            
        cnt, inc = 0, 0
        x = x0
        
        for x in range(x0, n+M):
            f = freq[x]
            cnt += (f != 0)
            
            if f <= 1: continue
            
            freq[x+1] += (f - 1)
            inc += (f - 1)
            
            if cnt >= n : break
            
        return inc
    
    
class Solution2:
    # Best / Most Optimal Solution
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dp = [0]*(max(nums)+ 1)
        
        for num in nums:
            dp[num] += 1

        count = 0
        
        for i in range(len(dp)-1):
            
            if dp[i] > 1:
                count += dp[i]-1
                dp[i+1] += (dp[i]-1)
                
        count += dp[-1]*(dp[-1]-1)//2
        
        return count 
