from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import heapq

# My Solution
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        pq = [(-1.0, start)]    
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:

                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0

# Best / Most Optimal Solution
class Solution:
    def dijkstras(self, graph, start, end):
        visited = set()
        heap = [(-1, start)]
        while heap:
            val, node = heappop(heap)
            val = -val
            if node == end:
                return val
            if node in visited:
                continue
            visited.add(node)
            for neigh_val, neigh_node in graph[node]:
                if neigh_node not in visited:
                    heappush(heap, (-val * neigh_val, neigh_node))
        return 0
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dict_graph = defaultdict(list)
        for e in range(len(edges)):
            i, j = edges[e]
            k = succProb[e]
            dict_graph[i].append((k,j))
            dict_graph[j].append((k,i))
        return self.dijkstras(dict_graph, start_node, end_node)
        