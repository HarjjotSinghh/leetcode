from collections import defaultdict, deque
from typing import List


# My Solution
class Solution:
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0
        for current_node in range(n - 2, -1, -1):
            min_distance = n
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            dp[current_node] = min_distance
        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            adj_list[i].append(i + 1)
        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)
            answer.append(self.find_min_distance(adj_list, n))
        return answer


# Best / Most Optimal Solution
class Solution2:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj = defaultdict(list)
        for i in range(n - 1):
            adj[i].append(i + 1)
        depth = [i for i in range(n)]

        def bfs(node):
            q = deque([node])
            while q:
                n = q.popleft()
                for nei in adj[n]:
                    if depth[nei] > depth[n] + 1:
                        depth[nei] = depth[n] + 1
                        q.append(nei)

        ans = []
        for s, e in queries:
            adj[s].append(e)
            if depth[e] > depth[s] + 1:
                depth[e] = depth[s] + 1
                bfs(e)
            ans.append(depth[-1])
        return ans
