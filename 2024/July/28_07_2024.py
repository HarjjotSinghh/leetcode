from heapq import heappush, heappop
from math import inf
from typing import List
from collections import deque

# My Solution
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        dist1 = [inf] * (n+1)
        dist2 = [inf] * (n+1)
        freq = [0] * (n+1)
        minHeap = []
        heappush(minHeap, (0,1))
        dist1[1] = 0
        while minHeap:
            timeTaken, node = heappop(minHeap)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken += time
            for neighbor in adj[node]:
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heappush(minHeap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heappush(minHeap, (timeTaken, neighbor))
        return 0

# Best / Most Optimal Solution
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while q:
            x, freq = q.popleft()
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time
            for y in g[x]:
                if dist1[y] == -1:
                    dist1[y] = t
                    q.append((y, 1))
                elif dist2[y] == -1 and dist1[y] != t:
                    if y == n:
                        return t
                    dist2[y] = t
                    q.append((y, 2))
        return 0
