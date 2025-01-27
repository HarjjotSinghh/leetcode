from collections import defaultdict
from typing import List


# My Solution
class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        for edge in prerequisites:
            isPrerequisite[edge[0]][edge[1]] = True
        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (
                        isPrerequisite[src][intermediate]
                        and isPrerequisite[intermediate][target]
                    )
        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])
        return answer


# Best / Most Optimal Solution
class Solution2:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = defaultdict(list)
        for prereq, postreq in prerequisites:
            graph[prereq].append(postreq)
        postreq_set = [set() for _ in range(numCourses)]

        def dfs(course):
            for postreq in graph[course]:
                if postreq not in postreq_set[course]:
                    postreq_set[course].add(postreq)
                    postreq_set[course].update(dfs(postreq))
            return postreq_set[course]

        for i in range(numCourses):
            dfs(i)

        res = []
        for prereq, postreq in queries:
            if postreq not in postreq_set[prereq]:
                res.append(False)
            else:
                res.append(True)
        return res
