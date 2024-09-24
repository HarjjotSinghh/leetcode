
# My Solution
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
        first_half = int(n[: i + 1])
        possibilities = []
        possibilities.append(
            self.half_to_palindrome(first_half, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half + 1, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half - 1, len_n % 2 == 0)
        )
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10**len_n + 1)
        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)
    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = res * 10 + left % 10
            left //= 10
        return res

# Best / Most Optimal Solution
class Solution2:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) < 10:
            return str(int(n) - 1)
        elif n == '1' + '0' * (len(n) - 1):
            return str(int(n) - 1)
        length = len(n)
        if length % 2 == 0:
            lstr = n[:length // 2]
            lnum = int(lstr)
        else:
            lstr = n[:length // 2 + 1]
            lnum = int(lstr)
        candidates = set()
        for diff in [-1, 0, 1]:
            curr_left = lnum + diff
            if length % 2 == 0:
                right = str(curr_left)
                candidates.add(str(curr_left) + right[::-1])
            else:
                right = str(curr_left)
                candidates.add(str(curr_left) + right[-2::-1])
        temp1 = '1' + '0' * (len(n) - 1) + '1'
        temp2 = '9' * (len(n) - 1)
        candidates.add(temp1)
        candidates.add(temp2)
        candidates.discard(n)
        min_diff = float('inf')
        nearest_palindrome = ""
        for can in candidates:
            diff = abs(int(can) - int(n))
            if diff < min_diff or (diff == min_diff and int(can) < int(nearest_palindrome)):
                min_diff = diff
                nearest_palindrome = can
        return nearest_palindrome
