from collections import deque
from typing import List


# My Solution
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        for person in range(n):
            in_degree[favorite[person]] += 1
        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        depth = [1] * n
        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
        longest_cycle = 0
        two_cycle_invitations = 0
        for person in range(n):
            if in_degree[person] == 0:
                continue
            cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0
                cycle_length += 1
                current = favorite[current]
            if cycle_length == 2:
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)
        return max(longest_cycle, two_cycle_invitations)


# Best / Most Optimal Solution
class Solution2:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        levels = [1] * n
        indegree = [0] * n
        for i in range(n):
            indegree[favorite[i]] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            neighbor = favorite[node]
            indegree[neighbor] -= 1
            levels[neighbor] = levels[node] + 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
        longest_path = max_perimeter = 0
        for i in range(n):
            if indegree[i] != 0:
                circle_start = circle_node = i
                indegree[circle_node] -= 1
                circle_perimeter = 1
                while favorite[circle_node] != circle_start:
                    circle_node = favorite[circle_node]
                    indegree[circle_node] -= 1
                    circle_perimeter += 1
                if circle_perimeter == 2:
                    longest_path += levels[circle_start] + levels[circle_node]
                else:
                    max_perimeter = max(max_perimeter, circle_perimeter)
        return max(max_perimeter, longest_path)
