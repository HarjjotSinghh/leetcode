from typing import List
from collections import Counter

# My Solution
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w, c in Counter((s1 + " " + s2).split()).items() if c == 1]

# Best / Most Optimal Solution
class Solution2:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count1 = Counter(s1.split(" "))
        count2 = Counter(s2.split(" "))
        set1 = [w1 for w1 in count1.keys() if count1[w1] <= 1 and count2[w1] <= 1]
        set2 = [w2 for w2 in count2.keys() if count1[w2] <= 1 and count2[w2] <= 1]
        return list(set(set1) - set(set2)) + list(set(set2) - set(set1))
