from typing import List

# My Solution
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        l = list(sorted(s))
        d = {}
        for i,k in enumerate(l):
            d[k]=i+1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr

# Best / Most Optimal Solution
class Solution2:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        b=sorted(set(arr))
        c={ele:rank+1 for rank,ele in enumerate(b)}
        ranked_arr=[c[ele] for ele in arr]
        return ranked_arr
