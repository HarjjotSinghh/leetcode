from typing import List
from operator import mul


# My Solution
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * n
        for a, b in roads:
            arr[a] += 1
            arr[b] += 1
        return sum(map(mul, sorted(arr), range(1, 1 + n)))


# Best / Most Optimal Solution
class Solution2:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        Arr = [0] * n
        for A, B in roads:
            Arr[A] += 1
            Arr[B] += 1
        Arr.sort()
        summ = 0
        for i in range(len(Arr)):
            summ += Arr[i] * (i + 1)
        return summ
