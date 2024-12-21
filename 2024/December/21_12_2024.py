from typing import List
from collections import defaultdict

# My Solution
class Solution:
    def maxKDivisibleComponents(self, N: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = defaultdict(list)
        indegrees = [0] * N
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1
        level = [i for i in range(N) if indegrees[i] <= 1]
        count = 0
        while level:
            nxt_level = set()
            for p in level:
                if values[p] >= 0 and values[p] % k == 0:
                    count += 1
                    values[p] = -1
                for nei in adj_list[p]:
                    if values[p] >= 0: values[nei] += values[p]
                    indegrees[nei] -= 1
                    if indegrees[nei] == 1:
                        nxt_level.add(nei)
            level = nxt_level
        return count

# Best / Most Optimal Solution
class Solution2:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        def dfs(i: int, fa: int) -> int:
            s = values[i]
            for j in g[i]:
                if j != fa:
                    s += dfs(j, i)
            nonlocal ans
            ans += s % k == 0
            return s
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans
