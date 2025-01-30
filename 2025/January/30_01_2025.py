from collections import defaultdict, deque
from typing import List


# My Solution
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            X, Y = find(x), find(y)
            if X != Y:
                parent[Y] = X

        for a, b in edges:
            union(a - 1, b - 1)
        valid = [-1] * n
        Max = defaultdict(int)
        for start in range(n):
            root = find(start)
            if valid[start] != -1:
                continue
            queue = deque([start])
            valid[start] = 0
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if valid[nei] == -1:
                        valid[nei] = 1 - valid[node]
                        queue.append(nei)
                    elif valid[nei] == valid[node]:
                        return -1

            def bfs(src):
                queue = deque([src])
                visited = [-1] * n
                visited[src] = 1
                max_depth = 1
                while queue:
                    node = queue.popleft()
                    for nei in adj[node]:
                        if visited[nei] == -1:
                            visited[nei] = visited[node] + 1
                            max_depth = max(max_depth, visited[nei])
                            queue.append(nei)
                return max_depth

            max_depth = 0
            for node in range(n):
                if find(node) == root:
                    max_depth = max(max_depth, bfs(node))
            Max[root] = max_depth
        return sum(Max.values())


# Best / Most Optimal Solution
class Solution2:
    def is_bipartite(self, adj_list, node, colors):
        for neighbor in adj_list[node]:
            if colors[neighbor] == colors[node]:
                return False
            if colors[neighbor] != -1:
                continue
            colors[neighbor] = (colors[node] + 1) % 2
            if not self.is_bipartite(adj_list, neighbor, colors):
                return False
        return True

    def get_longest_shortest_path(self, adj_list, src_node, n):
        nodes_queue = deque([src_node])
        visited = [False] * n
        visited[src_node] = True
        distance = 0
        while nodes_queue:
            for _ in range(len(nodes_queue)):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
            distance += 1
        return distance

    def get_number_of_groups_for_component(self, adj_list, node, distances, visited):
        max_number_of_groups = distances[node]
        visited[node] = True
        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue
            max_number_of_groups = max(
                max_number_of_groups,
                self.get_number_of_groups_for_component(
                    adj_list, neighbor, distances, visited
                ),
            )
        return max_number_of_groups

    def magnificentSets(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        colors = [-1] * n
        for node in range(n):
            if colors[node] != -1:
                continue
            colors[node] = 0
            if not self.is_bipartite(adj_list, node, colors):
                return -1
        distances = [
            self.get_longest_shortest_path(adj_list, node, n) for node in range(n)
        ]
        max_number_of_groups = 0
        visited = [False] * n
        for node in range(n):
            if visited[node]:
                continue
            max_number_of_groups += self.get_number_of_groups_for_component(
                adj_list, node, distances, visited
            )
        return max_number_of_groups
