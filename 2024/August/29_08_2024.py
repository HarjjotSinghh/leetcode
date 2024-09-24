from typing import List

# My Solution
class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind(
            20002
        )
        for x, y in stones:
            uf._union_nodes(
                x, y + 10001
            )
        return len(stones) - uf.component_count
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n
            self.component_count = (
                0
            )
            self.unique_nodes = (
                set()
            )
        def _find(self, node):
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)
            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]
        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)
            if root1 == root2:
                return
            self.parent[root1] = root2
            self.component_count -= 1

# Best / Most Optimal Solution
class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rank = [1] * n
        parent = [i for i in range(n)]
        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return 0
            if rank[i] < rank[j]:
                i, j = j, i
            rank[i] += rank[j]
            parent[j] = parent[i]
            return 1
        def find(i):
            while i != parent[i]:
                parent[i] = i = parent[parent[i]]
            return i
        rows, cols = {}, {}
        removed = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removed += union(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += union(i, cols[col])
            else:
                cols[col] = i
        return removed
