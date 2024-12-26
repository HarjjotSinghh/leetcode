import heapq
from typing import List

# My Solution
class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        max_idx = []
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]
        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )
        for idx, height in enumerate(heights):
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)
        return results

# Best / Most Optimal Solution
class Solution2:
    def leftmostBuildingQueries(self, H: List[int], queries: List[List[int]]) -> List[int]:
        Q = []
        res = [-1]*len(queries)
        store = [[] for _ in H]
        for k, (i, j) in enumerate(queries):
            if i < j and H[i] < H[j]: res[k] = j
            elif i > j and H[i] > H[j]: res[k] = i
            elif i == j: res[k] = i
            else:
                store[max(i, j)].append((max(H[i], H[j]), k))
        for i, h in enumerate(H):
            while Q and Q[0][0] < h:
                res[heapq.heappop(Q)[1]] = i
            for s in store[i]:
                heapq.heappush(Q, s)
        return res
