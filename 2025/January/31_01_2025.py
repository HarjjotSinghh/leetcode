from typing import List


# My Solution
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find(u):
            if u == parent[u]:
                return u
            else:
                parent[u] = find(parent[u])
                return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if size[pv] > size[pu]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        n = len(grid)
        parent = [i for i in range(n * n)]
        size = [1 for i in range(n * n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    a = i * n + j
                    for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= u < n and 0 <= v < n and grid[u][v]:
                            b = u * n + v
                            union(a, b)
        m = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    t = set()
                    c = 1
                    for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= u < n and 0 <= v < n and grid[u][v]:
                            a = u * n + v
                            t.add(find(a))
                    for x in t:
                        c += size[x]
                    if c > m:
                        m = c
        for i in range(n * n):
            m = max(m, size[find(i)])
        return m


# Best / Most Optimal Solution
class Solution2:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        id = 2
        sz = {}

        def dfs(row, col, isl_id):
            grid[row][col] = isl_id
            size = 1
            if row != 0:
                if grid[row - 1][col] == 1:
                    size += dfs(row - 1, col, isl_id)
            if col != 0:
                if grid[row][col - 1] == 1:
                    size += dfs(row, col - 1, isl_id)
            if row != n - 1:
                if grid[row + 1][col] == 1:
                    size += dfs(row + 1, col, isl_id)
            if col != n - 1:
                if grid[row][col + 1] == 1:
                    size += dfs(row, col + 1, isl_id)
            return size

        for i in range(n):
            for j in range(n):
                ts = 0
                if grid[i][j] == 1:
                    ts = dfs(i, j, id)
                    sz[id] = ts
                    id += 1
        if not sz:
            return 1
        res = max(sz.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    sn = set()
                    p = 1
                    if i != 0:
                        if grid[i - 1][j] > 1:
                            t = grid[i - 1][j]
                            if t not in sn:
                                p += sz[t]
                                sn.add(t)
                    if i != n - 1:
                        if grid[i + 1][j] > 1:
                            t = grid[i + 1][j]
                            if t not in sn:
                                p += sz[t]
                                sn.add(t)
                    if j != 0:
                        if grid[i][j - 1] > 1:
                            t = grid[i][j - 1]
                            if t not in sn:
                                p += sz[t]
                                sn.add(t)
                    if j != n - 1:
                        if grid[i][j + 1] > 1:
                            t = grid[i][j + 1]
                            if t not in sn:
                                p += sz[t]
                                sn.add(t)
                    res = max(res, p)
        return res
