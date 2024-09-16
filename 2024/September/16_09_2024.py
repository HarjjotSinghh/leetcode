from typing import List

# My Solution
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * (24 * 60)
        for time in timePoints:
            h, m = map(int, time.split(":"))
            min_time = h * 60 + m
            if minutes[min_time]:
                return 0
            minutes[min_time] = True
        prevIndex = float("inf")
        firstIndex = float("inf")
        lastIndex = float("inf")
        ans = float("inf")
        for i in range(24 * 60):
            if minutes[i]:
                if prevIndex != float("inf"):
                    ans = min(ans, i - prevIndex)
                prevIndex = i
                if firstIndex == float("inf"):
                    firstIndex = i
                lastIndex = i
        return min(ans, 24 * 60 - lastIndex + firstIndex)

# Best / Most Optimal Solution
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        s = set()
        def transform(i):
            t = i.split(":")
            return int(t[0])*60 + int(t[1])
        
        points = []
        for i in timePoints:
            p = transform(i)
            if p in s:
                return 0
            s.add(p)
            points.append(transform(i))
        points.sort()
        m = 24*60 - points[-1] + points[0]
        for i in range(len(points)-1):
            m = min(m, points[i+1]-points[i])
        return m
