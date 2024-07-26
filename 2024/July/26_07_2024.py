from typing import List
from collections import deque
from heapq import heapify, heappop, heappush

# My Solution
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adjacency_list = [[] for _ in range(n)]
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            shortest_path_matrix[i][i] = 0
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))
        for i in range(n):
            self.spfa(n, adjacency_list, shortest_path_matrix[i], i)
        return self.get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )
    def spfa(
        self,
        n: int,
        adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int],
        source: int,
    ):
        queue = deque([source])
        update_count = [0] * n
        shortest_path_distances[:] = [float("inf")] * n
        shortest_path_distances[source] = 0
        while queue:
            current_city = queue.popleft()
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if (
                    shortest_path_distances[neighbor_city]
                    > shortest_path_distances[current_city] + edge_weight
                ):
                    shortest_path_distances[neighbor_city] = (
                        shortest_path_distances[current_city] + edge_weight
                    )
                    update_count[neighbor_city] += 1
                    queue.append(neighbor_city)
                    if update_count[neighbor_city] > n:
                        print("Negative weight cycle detected")
    def get_city_with_fewest_reachable(
        self,
        n: int,
        shortest_path_matrix: List[List[int]],
        distance_threshold: int,
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and shortest_path_matrix[i][j] <= distance_threshold
            )
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable

# Best / Most Optimal Solution
class Solution2:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = {i:dict() for i in range(n)}
        for u, v, d in edges:
            if d <= distanceThreshold:
                adj[u][v] = d
                adj[v][u] = d
        cities = [0] * n
        for i in range(n):
            count = -1
            distance = [float('inf')] * n
            distance[i] = 0
            visited = [False] * n
            pq = [(0, i)]
            heapify(pq)
            while pq:
                d, node = heappop(pq)
                if d > distanceThreshold:
                    break
                if visited[node]:
                    continue
                visited[node] = True
                count += 1
                for v in adj[node]:
                    if not visited[v] and d + adj[node][v] < distance[v]:
                        distance[v] = d + adj[node][v]
                        heappush(pq, (distance[v], v))
            cities[i] = count
        max_node = 0
        min_distnace = cities[0]
        for i in range(n):
            if cities[i] <= min_distnace:
                max_node = i
                min_distnace = cities[i]
        return max_node
