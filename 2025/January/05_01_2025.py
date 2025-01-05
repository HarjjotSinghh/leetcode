from typing import List


# My Solution
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_array = [0] * n
        for shift in shifts:
            if shift[2] == 1:
                diff_array[shift[0]] += 1
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] -= 1
            else:
                diff_array[shift[0]] -= 1
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] += 1
        result = list(s)
        number_of_shifts = 0
        for i in range(n):
            number_of_shifts = (number_of_shifts + diff_array[i]) % 26
            if number_of_shifts < 0:
                number_of_shifts += 26
            shifted_char = chr(
                (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
            )
            result[i] = shifted_char
        return "".join(result)


# Best / Most Optimal Solution
class Solution2:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0] * (len(s) + 1)
        for st, en, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[en + 1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[en + 1] -= 1
        cum_sum = 0
        s = list(s)
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s[i] = chr(new_code)
        return "".join(s)
