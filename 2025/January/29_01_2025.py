from typing import List


# My Solution
class Solution:
    def is_connected(self, src, target, visited, adj_list):
        visited[src] = True
        if src == target:
            return True
        is_found = False
        for adj in adj_list[src]:
            if not visited[adj]:
                is_found = is_found or self.is_connected(adj, target, visited, adj_list)
        return is_found

    def findRedundantConnection(self, edges):
        N = len(edges)
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            visited = [False] * N
            if self.is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        return []


# Best / Most Optimal Solution
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
