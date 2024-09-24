from typing import List

# My Solution
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefixes = set()
        for val in arr1:
            while val not in arr1_prefixes and val > 0:
                arr1_prefixes.add(val)
                val //= 10
        longest_prefix = 0
        for val in arr2:
            while val not in arr1_prefixes and val > 0:
                val //= 10
            if val > 0:
                longest_prefix = max(longest_prefix, len(str(val)))
        return longest_prefix

# Best / Most Optimal Solution
class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        flag_s = set()
        for i in arr1:
            while i:
                flag_s.add(i)
                i //= 10
        ans = 0
        for i in arr2:
            while i:
                if i in flag_s:
                    break
                i //= 10
            if i:
                ans = max(ans, len(str(i)))
        return ans
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    i = 0
    args = []
    for a in inputs:
        i += 1
        args.append(a)
        if i & 1:
            continue
        print(str(Solution().longestCommonPrefix(*args)).replace(" ", ""), file=f)
        args = []
exit(0)

