from typing import List

# My Solution
class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)
        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        for i in range(1, maxAbility + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        return netProfit

# Best / Most Optimal Solution
class Solution2:
    def maxProfitAssignment(self, d: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(d, profit))
        worker.sort()
        ans = j = maxp = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                maxp = max(maxp, jobs[j][1])
                j+=1
            ans += maxp
        return ans
