from typing import List


# My Solution
class Solution:
    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visit = [False] * n
        inStack = [False] * n
        for i in range(n):
            self.dfs(i, graph, visit, inStack)
        safeNodes = []
        for i in range(n):
            if not inStack[i]:
                safeNodes.append(i)
        return safeNodes


# Best / Most Optimal Solution
class Solution2:
    def __init__(self):
        self.output = []

    def has_cycle(self, graph, path, visited, node):
        visited[node] = True
        path[node] = True
        for nei in graph[node]:
            if path[nei]:
                return True

            if not visited[nei]:
                if self.has_cycle(graph, path, visited, nei):
                    return True

        path[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path = [False] * n
        self.output = [True] * n
        for i in range(n):
            if not visited[i]:
                self.has_cycle(graph, path, visited, i)
        final = []
        for i in range(n):
            if not path[i]:
                final.append(i)
        return final
