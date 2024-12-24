from collections import defaultdict
from typing import List
from collections import deque

# My Solution
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find_optimal_max_radius(adj_list):
            in_deg = {k: len(v) for k, v in adj_list.items()}
            stack = set(k for k, v in in_deg.items() if v == 1)
            ans = 0
            while len(stack) > 1:
                new_stack = set()
                for a in stack:
                    for b in adj_list[a]:
                        in_deg[b] -= 1
                        if in_deg[b] == 1:
                            new_stack.add(b)
                stack = new_stack
                ans += 1
            return ans, ans * 2 - (0 if len(stack) else 1)
        adj_list1, adj_list2 = defaultdict(set), defaultdict(set)
        for a, b in edges1:
            adj_list1[a].add(b)
            adj_list1[b].add(a)
        for a, b in edges2:
            adj_list2[a].add(b)
            adj_list2[b].add(a)
        max_rad_1, diam_1 = find_optimal_max_radius(adj_list1)
        max_rad_2, diam_2 = find_optimal_max_radius(adj_list2)
        ans = max_rad_1 + max_rad_2 + 1
        ans = max(ans, diam_1)
        ans = max(ans, diam_2)
        return ans

# Best / Most Optimal Solution
class Solution2:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        d1 = self.get_diameter(n, edges1)
        r1 = (d1 + 1) // 2
        d2 = self.get_diameter(m, edges2)
        r2 = (d2 + 1) // 2
        return max(d1, d2, 1 + r1 + r2)
    def get_diameter(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
            degree[v] += 1
            degree[w] += 1
        leaves = deque(v for v in range(n) if degree[v] == 1)
        tree_size = n
        radius = 0
        while tree_size > 2:
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                tree_size -= 1
                degree[leaf] -= 1
                for nxt in graph[leaf]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        leaves.append(nxt)
            radius += 1
        return 2 * radius + (tree_size == 2)
