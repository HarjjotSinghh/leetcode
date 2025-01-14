from typing import List


# My Solution
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        frequency = [0 for _ in range(n + 1)]
        common_count = 0
        for current_index in range(n):
            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                common_count += 1
            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                common_count += 1
            prefix_common_array[current_index] = common_count
        return prefix_common_array


# Best / Most Optimal Solution
class Solution2:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        seta, setb = set(), set()
        for i in range(n):
            C[i] = C[i - 1]
            if A[i] == B[i]:
                C[i] += 1
            else:
                if A[i] in setb:
                    C[i] += 1
                if B[i] in seta:
                    C[i] += 1
                seta.add(A[i])
                setb.add(B[i])
        return C
