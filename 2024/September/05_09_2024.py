from typing import List
import sys
from json import loads, dumps


# My Solution
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements

# Best / Most Optimal Solution
class Solution2:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        totalSum = mean * (m + n)
        rollsSum = sum(rolls)
        missingSum = totalSum - rollsSum
        if missingSum < n or missingSum > 6 * n:
            return []
        quotient, remainder = divmod(missingSum, n)
        return [quotient + (1 if i < remainder else 0) for i in range(n)]
def main():
    inputs = map(loads, sys.stdin)
    results = []
    while True:
        try:
            rolls = next(inputs)
            mean = next(inputs)
            n = next(inputs)
            result = Solution().missingRolls(rolls, mean, n)
            results.append(result)
        except StopIteration:
            break
    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)
if __name__ == "__main__":
    main()
    sys.exit(0)
