from typing import List

# My Solution
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        r_min_max = float('-inf')
        for i in range(N):
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)
        c_max_min = float('inf')
        for i in range(M):
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)
        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
        
# Best / Most Optimal Solution
class Solution2:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])
        numIdxMap = {}
        result = []
        for i in range(R):
            row = matrix[i]
            minColIdx = row.index(min(matrix[i]))
            minValInRow = matrix[i][minColIdx]
            isLuckyNum = True
            for r in range(R):
                if r != i and matrix[r][minColIdx] > minValInRow:
                    isLuckyNum = False
                    break
            if isLuckyNum:
                result.append(minValInRow)
        return result
