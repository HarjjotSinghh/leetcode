from typing import List
from math import inf


# My Solution
class Solution:
    def __init__(self):
        self.tree = []
        self.distance_from_bob = []
        self.n = 0

    def mostProfitablePath(self, edges, bob, amount):
        self.n = len(amount)
        self.tree = [[] for _ in range(self.n)]
        self.distance_from_bob = [0] * self.n
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])
        return self.find_paths(0, 0, 0, bob, amount)

    def find_paths(self, source_node, parent_node, time, bob, amount):
        max_income = 0
        max_child = float("-inf")
        if source_node == bob:
            self.distance_from_bob[source_node] = 0
        else:
            self.distance_from_bob[source_node] = self.n
        for adjacent_node in self.tree[source_node]:
            if adjacent_node != parent_node:
                max_child = max(
                    max_child,
                    self.find_paths(adjacent_node, source_node, time + 1, bob, amount),
                )
                self.distance_from_bob[source_node] = min(
                    self.distance_from_bob[source_node],
                    self.distance_from_bob[adjacent_node] + 1,
                )
        if self.distance_from_bob[source_node] > time:
            max_income += amount[source_node]
        elif self.distance_from_bob[source_node] == time:
            max_income += amount[source_node] // 2
        return max_income if max_child == float("-inf") else max_income + max_child


# Best / Most Optimal Solution
class Solution2:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        bob_time = [n] * n

        def dfs_bob(x: int, fa: int, t: int) -> bool:
            if x == 0:
                bob_time[x] = t
                return True
            for y in g[x]:
                if y != fa and dfs_bob(y, x, t + 1):
                    bob_time[x] = t
                    return True
            return False

        dfs_bob(bob, -1, 0)
        g[0].append(-1)
        ans = -inf

        def dfs_alice(x: int, fa: int, alice_time: int, tot: int) -> None:
            if alice_time < bob_time[x]:
                tot += amount[x]
            elif alice_time == bob_time[x]:
                tot += amount[x] // 2
            if len(g[x]) == 1:
                nonlocal ans
                ans = max(ans, tot)
                return
            for y in g[x]:
                if y != fa:
                    dfs_alice(y, x, alice_time + 1, tot)

        dfs_alice(0, -1, 0, 0)
        return ans
