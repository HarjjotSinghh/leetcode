
# My Solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1

# Best / Most Optimal Solution
class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        else:
            return (self.findTheWinner(n-1, k)+k-1) % n + 1
