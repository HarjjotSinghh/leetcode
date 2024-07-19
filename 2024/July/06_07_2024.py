# My Solution
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_rounds = time // (n - 1)
        extra_time = time % (n - 1)
        if full_rounds % 2 == 0:
            return extra_time + 1
        else:
            return n - extra_time
        
# Best / Most Optimal Solution
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        left_to_right = True
        pos = 1
        for i in range(1, time+1):
            if left_to_right:
                pos += 1
            else:
                pos -= 1
            if i%(n-1) == 0:
                left_to_right = not left_to_right
        return pos
