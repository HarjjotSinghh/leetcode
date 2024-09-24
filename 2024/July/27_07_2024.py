from typing import List
from collections import defaultdict
from heapq import heappush, heappop
from math import inf

# My Solution
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        total_cost = 0
        min_cost = [[float("inf")] * 26 for _ in range(26)]
        for orig, chg, cst in zip(original, changed, cost):
            start_char = ord(orig) - ord("a")
            end_char = ord(chg) - ord("a")
            min_cost[start_char][end_char] = min(
                min_cost[start_char][end_char], cst
            )
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(
                        min_cost[i][j], min_cost[i][k] + min_cost[k][j]
                    )
        for src, tgt in zip(source, target):
            if src == tgt:
                continue
            source_char = ord(src) - ord("a")
            target_char = ord(tgt) - ord("a")
            if min_cost[source_char][target_char] == float("inf"):
                return -1
            total_cost += min_cost[source_char][target_char]
        return total_cost

# Best / Most Optimal Solution
class Solution:
    def minimumCostFrom(self, sourceChar):
        bests = {}
        seenCost = defaultdict(lambda: inf)
        seenCost[sourceChar] = 0
        frontier = [(0, sourceChar)]
        while len(frontier) > 0:
            reachCost, current = heappop(frontier)
            if current in bests:
                continue
            bests[current] = reachCost
            for d, edgeCost in self.edges[current].items():
                totalCost = reachCost + edgeCost
                if totalCost < seenCost[d]:
                    heappush(frontier, (totalCost, d))
                    seenCost[d] = totalCost
        return bests
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.edges = defaultdict(lambda: {})
        for i in range(len(original)):
            s = original[i]
            d = changed[i]
            c = cost[i]
            if d not in self.edges[s] or c < self.edges[s][d]:
                self.edges[s][d] = c
        bests = defaultdict(lambda: {})
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                if t in bests[s]:
                    totalCost += bests[s][t]
                elif len(bests[s]) > 0:
                    return -1
                else:
                    best = self.minimumCostFrom(s)
                    bests[s] = best
                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1
        return totalCost
