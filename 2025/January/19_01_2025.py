import heapq
from typing import List


# My Solution
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        water_trapped = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    water_trapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        return water_trapped


# Best / Most Optimal Solution
class Solution2:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M = len(heightMap)
        N = len(heightMap[0])
        h = []
        for i in [0, M - 1]:
            for j in range(N):
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1
        for i in range(1, M - 1):
            for j in [0, N - 1]:
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1
        heapq.heapify(h)
        tot = 0
        while h:
            height, x, y = heapq.heappop(h)
            stack = [(x, y)]
            while h and h[0][0] == height:
                _, x, y = heapq.heappop(h)
                stack.append((x, y))
            while stack:
                x, y = stack.pop()
                for d in [-1, 1]:
                    nX = x + d
                    nY = y + d
                    if 0 < nX < M - 1 and heightMap[nX][y] != -1:
                        if height > heightMap[nX][y]:
                            tot += height - heightMap[nX][y]
                            stack.append((nX, y))
                            heightMap[nX][y] = -1
                        else:
                            heapq.heappush(h, (heightMap[nX][y], nX, y))
                            heightMap[nX][y] = -1

                    if 0 < nY < N - 1 and heightMap[x][nY] != -1:
                        if height > heightMap[x][nY]:
                            tot += height - heightMap[x][nY]
                            stack.append((x, nY))
                            heightMap[x][nY] = -1
                        else:
                            heapq.heappush(h, (heightMap[x][nY], x, nY))
                            heightMap[x][nY] = -1
        return tot
