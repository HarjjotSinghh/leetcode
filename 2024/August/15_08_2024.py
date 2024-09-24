from typing import List
from sys import stdin
from json import loads

# My Solution
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0
        for customer_bill in bills:
            if customer_bill == 5:
                five_dollar_bills += 1
            elif customer_bill == 10:
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            else:
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        return True

# Best / Most Optimal Solution
class Solution2:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return "false"
        return "true"

s = Solution2()
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{s.lemonadeChange(case)}\n")
exit(0)
