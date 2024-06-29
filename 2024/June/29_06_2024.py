from typing import List
from collections import deque, defaultdict

# My Solution         
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        indegrees = [0] * n
        for e in edges:
            g[e[0]].append(e[1])
            indegrees[e[1]] += 1
        queue = deque()
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
        r = [set() for _ in range(n)]
        while queue:
            i = queue.popleft()
            for j in g[i]:
                r[j].add(i)
                r[j].update(r[i])
                indegrees[j] -= 1
                if not indegrees[j]:
                    queue.append(j)
        ret = [sorted(list(s)) for s in r]
        return ret

# Best / Most Optimal Solution
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in edges:
            d[i[1]].append(i[0])
        ans = [None for i in range(n)]
        def dfs(i):
            res = set()
            for j in d[i]:
                if ans[j] is None:
                    dfs(j)
                res.update(ans[j])
            res.update(d[i])
            ans[i] = res
        for i in range(n):
            if ans[i] is None:
                dfs(i)
        for i in range(n):
            ans[i] = list(ans[i])
            ans[i].sort()
        return ans
