from typing import List


# My Solution
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1
        champ = -1
        champ_count = 0
        for i in range(n):
            if indegree[i] == 0:
                champ_count += 1
                champ = i
        return champ if champ_count == 1 else -1


# Best / Most Optimal Solution
class Solution2:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        can_win = [True] * n
        for a, b in edges:
            can_win[b] = False
        winner = -1
        winner_count = 0
        for i in range(0, n):
            if can_win[i]:
                winner = i
                winner_count += 1
        if winner_count == 1:
            return winner
        return -1
