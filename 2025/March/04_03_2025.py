from cmath import log

# My Solution
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

# Best / Most Optimal Solution
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        lastPowUsed = None
        while n != 0:
            logResult = log(n, 3)
            decimalPart = logResult % 1
            integerPart = int(logResult - decimalPart)
            integerPart += 1 if decimalPart > 0.999 else 0
            if integerPart == lastPowUsed: return False
            lastPowUsed = integerPart
            n -= 3**integerPart
        return True
