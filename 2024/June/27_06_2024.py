from typing import List

# My Solution
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if not edges:
            return None
        common_elements = set(edges[0])
        for array in edges[1:]:
            common_elements &= set(array)
        common_elements = list(common_elements)
        return common_elements[0] if common_elements else None
    
# Best / Most Optimal Solution
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        o = edges[0][0]
        return o if o in edges[1] else edges[0][1]
