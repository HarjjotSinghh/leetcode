from typing import List
from collections import defaultdict

# My Solution
class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = (
            60001
        )
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0
        for command in commands:
            if command == -1:
                current_direction = (current_direction + 1) % 4
                continue
            if command == -2:
                current_direction = (current_direction + 3) % 4
                continue
            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y
            max_distance_squared = max(max_distance_squared, x * x + y * y)
        return max_distance_squared
    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.HASH_MULTIPLIER * y

# Best / Most Optimal Solution
class Solution2:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        at_x = defaultdict(list)
        at_y = defaultdict(list)
        for obs in obstacles:
            at_x[obs[0]].append(obs[1])
            at_y[obs[1]].append(obs[0])
        cur_dir_x = 0
        coords = (0,0)
        max_dist = 0
        for com in commands:
            if com == -2:
                cur_dir_x = (cur_dir_x - 1) % 4 
                continue
            if com == -1:
                cur_dir_x = (cur_dir_x + 1) % 4
                continue
            if cur_dir_x == 0 or cur_dir_x == 2:
                relevant_obstacles = at_x[coords[0]]
                if relevant_obstacles:
                    if cur_dir_x == 0:
                        closest = 10**6
                        for rel_obs in relevant_obstacles:      
                            if rel_obs > coords[1]:
                                closest = min(closest, rel_obs)
                        coords = (coords[0], min(coords[1] + com, closest - 1))
                    else:
                        closest = -10**6
                        for rel_obs in relevant_obstacles:
                            if rel_obs < coords[1]:
                                closest = max(closest, rel_obs)
                        coords = (coords[0], max(coords[1] - com, closest + 1))
                else:
                    com = com if cur_dir_x == 0 else -com
                    coords = (coords[0], coords[1] + com)
            else:
                relevant_obstacles = at_y[coords[1]]
                if relevant_obstacles:
                    if cur_dir_x == 1:
                        closest = 10**6
                        for rel_obs in relevant_obstacles:
                            if rel_obs > coords[0]:
                                closest = min(closest, rel_obs)
                        coords = (min(coords[0] + com, closest - 1), coords[1])
                    else: 
                        closest = -10**6
                        for rel_obs in relevant_obstacles:
                            if rel_obs < coords[0]:
                                closest = max(closest, rel_obs)
                        coords = (max(coords[0] - com, closest + 1), coords[1])
                else:
                    com = com if cur_dir_x == 1 else -com
                    coords = (coords[0] + com, coords[1])
            max_dist = max(max_dist, coords[0]**2 + coords[1]**2)
        return max_dist
