from sortedcontainers import SortedDict
from typing import List

# My Solution
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        hashmap = SortedDict(int)
        for i,val in nums1+nums2:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i]+=val
        for key,val in hashmap.items():
            res.append([key,val])
        return res


# Best / Most Optimal Solution
class Solution2:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        left =0
        right=0
        ans =[]
        while left<len(nums1) and right<len(nums2):
            if nums1[left][0] == nums2[right][0]:
                ans.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
                left+=1
                right+=1
            elif nums1[left][0] < nums2[right][0]:
                ans.append(nums1[left])
                left+=1
            else:
                ans.append(nums2[right])
                right+=1 
        while left<len(nums1):
                ans.append(nums1[left])
                left+=1

        while right<len(nums2):
                ans.append(nums2[right])
                right+=1                    
        return ans          
        