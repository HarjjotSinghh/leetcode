from typing import List


# My Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return
        if target == 0:
            answer.append(path)
            return
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )

# Best / Most Optimal Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, cur, target):
            if target == 0 and cur[:] not in res:
                res.append(cur[:])
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                cur.append(candidates[i])
                backtrack(i+1, cur, target - candidates[i])
                cur.pop()
        backtrack(0, [], target)
        return res