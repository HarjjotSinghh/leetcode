from typing import List

# My Solution
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in range(len(details)):
            age = int(details[i][11:13])
            if age > 60:
                res += 1
        return res

# Best / Most Optimal Solution
class Solution2:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for people in details:
            if int(people[11:13]) > 60:
                count += 1
        return count
