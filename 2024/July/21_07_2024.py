from typing import List
# My Solution
class Solution:
    def buildMatrix(
        self,
        k: int,
        row_conditions: List[List[int]],
        col_conditions: List[List[int]],
    ) -> List[List[int]]:
        order_rows = self.__topo_sort(row_conditions, k)
        order_columns = self.__topo_sort(col_conditions, k)
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_columns[j]:
                    matrix[i][j] = order_rows[i]
        return matrix
    def __topo_sort(self, edges, n):
        adj = [[] for _ in range(n + 1)]
        deg = [0] * (n + 1)
        order = []
        for x in edges:
            adj[x[0]].append(x[1])
            deg[x[1]] += 1
        q = deque()
        for i in range(1, n + 1):
            if deg[i] == 0:
                q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n -= 1
            for v in adj[f]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        if n != 0:
            return []
        return order
    
# Best / Most Optimal Solution
class Solution2:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def f(cond):
            g = defaultdict(list)
            indeg = [0] * (k + 1)
            for a, b in cond:
                g[a].append(b)
                indeg[b] += 1
            q = deque([i for i, v in enumerate(indeg[1:], 1) if v == 0])
            res = []
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    res.append(i)
                    for j in g[i]:
                        indeg[j] -= 1
                        if indeg[j] == 0:
                            q.append(j)
            return None if len(res) != k else res

        row = f(rowConditions)
        col = f(colConditions)
        if row is None or col is None:
            return []
        ans = [[0] * k for _ in range(k)]
        m = [0] * (k + 1)
        for i, v in enumerate(col):
            m[v] = i
        for i, v in enumerate(row):
            ans[i][m[v]] = v
        return ans
