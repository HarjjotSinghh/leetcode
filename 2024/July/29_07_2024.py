from typing import List
import bisect

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for j in range(n):
            less_left = less_right = greater_left = greater_right = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                elif rating[i] > rating[j]:
                    greater_left += 1
            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                elif rating[k] > rating[j]:
                    greater_right += 1
            res += less_left * greater_right + greater_left * less_right
        return res

# Best / Most Optimal Solution
class Solution2:
    def numTeams(self, rating: List[int]) -> int:
        l = []
        sr = sorted(rating)
        low = {}
        for idx,r in enumerate(sr):
            low[r] = idx
        res = 0
        n = len(rating)
        for idx,r in enumerate(rating):
            i = bisect.bisect(l, r)
            l.insert(i,r)
            j = low[r] - i
            res+=i*(n-1-idx-j)+j*(idx-i)
        return res
