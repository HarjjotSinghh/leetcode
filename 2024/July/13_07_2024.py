from typing import List
from collections import deque

# My Solution
class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        result = []
        stack = deque()
        indices.sort(key=lambda x: positions[x])
        for current_index in indices:
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[current_index]:
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        healths[current_index] = 0
                        healths[top_index] = 0
        for index in range(n):
            if healths[index] > 0:
                result.append(healths[index])
        return result

# Best / Most Optimal Solution
class Solution2:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        left, right = [], []
        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            if directions[i] == 'R': right.append(i)
            else:
                while right and healths[right[-1]] < healths[i]:
                    right.pop()
                    healths[i] -= 1
                if not right: left.append(i)
                elif healths[right[-1]] == healths[i]: right.pop()
                else: healths[right[-1]] -= 1
        return [healths[i] for i in sorted(left+right)]