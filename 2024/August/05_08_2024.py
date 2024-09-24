from collections import Counter
from typing import List

# My Solution
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = ""
        c = Counter(arr)
        distinct = [x for x,y in c.items() if y==1]
        if len(distinct) < k:
            return res
        return distinct[k-1]

# Best / Most Optimal Solution
class Solution2:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=""
        n=0
        for i,j in d.items():
            if j==1:
                c=i
                n+=1
            if n==k:
                return i
        return ""
