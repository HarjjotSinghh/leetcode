# My Solution
class Solution:
    def can_partition(self, num, target):
        if target < 0 or num < target:
            return False
        if num == target:
            return True
        return (
            self.can_partition(num // 10, target - num % 10)
            or self.can_partition(num // 100, target - num % 100)
            or self.can_partition(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0
        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            if self.can_partition(square_num, current_num):
                punishment_num += square_num
        return punishment_num


# Best / Most Optimal Solution
class Solution2:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        l = [
            0,
            1,
            9,
            10,
            36,
            45,
            55,
            82,
            91,
            99,
            100,
            235,
            297,
            369,
            370,
            379,
            414,
            657,
            675,
            703,
            756,
            792,
            909,
            918,
            945,
            964,
            990,
            991,
            999,
            1000,
        ]
        for i in l:
            if i > n:
                break
            ans += i * i
        return ans
