import collections
from typing import List


# My Solution
class Solution:
    def validArrangement(self, pairs):
        adjacencyMatrix = collections.defaultdict(list)
        inDegree, outDegree = collections.defaultdict(int), collections.defaultdict(int)
        for pair in pairs:
            start, end = pair[0], pair[1]
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1
        result = []
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break
        if startNode == -1:
            startNode = pairs[0][0]
        nodeStack = [startNode]
        while nodeStack:
            node = nodeStack[-1]
            if adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].pop(0)
                nodeStack.append(nextNode)
            else:
                result.append(node)
                nodeStack.pop()
        result.reverse()
        pairedResult = []
        for i in range(1, len(result)):
            pairedResult.append([result[i - 1], result[i]])
        return pairedResult


# Best / Most Optimal Solution
class Solution2:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        inOutDeg = collections.defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1
            inOutDeg[end] -= 1
        startNode = pairs[0][0]
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break
        path = []

        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]
