from typing import List
from collections import deque
from math import inf


# My Solution
class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])
        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]
        for i in range(robot_count):
            dp[i][factory_count] = 1e12
        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]
                skip = dp[i][j + 1]
                dp[i][j] = min(assign, skip)
        return dp[0][0]


# Best / Most Optimal Solution
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][-1] = inf
        for j in range(n - 1, -1, -1):
            prefix = 0
            qq = deque([(m, 0)])
            for i in range(m - 1, -1, -1):
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i + factory[j][1]:
                    qq.popleft()
                while qq and qq[-1][1] >= dp[i][j + 1] - prefix:
                    qq.pop()
                qq.append((i, dp[i][j + 1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]
