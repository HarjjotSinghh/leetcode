from typing import List


# My Solution
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        digit_mapping = [0] * 82
        for element in nums:
            digit_sum = 0
            temp_element = element
            while temp_element:
                temp_element, curr_digit = divmod(temp_element, 10)
                digit_sum += curr_digit
            if digit_mapping[digit_sum] > 0:
                result = max(result, digit_mapping[digit_sum] + element)
            digit_mapping[digit_sum] = max(digit_mapping[digit_sum], element)
        return result


# Best / Most Optimal Solution
class Solution2:
    def maximumSum(self, nums: List[int]) -> int:
        d, mx = dict(), -1
        for num in nums:
            sm, n = 0, num
            while n:
                sm += n % 10
                n //= 10
            if sm in d:
                if d[sm][0] <= num:
                    d[sm][1] = d[sm][0]
                    d[sm][0] = num
                elif d[sm][1] < num:
                    d[sm][1] = num
            else:
                d[sm] = [num, -1]
        for k in d:
            if d[k][1] != -1:
                sm = d[k][0] + d[k][1]
                if sm > mx:
                    mx = sm
        return mx
