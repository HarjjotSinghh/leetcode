# My Solution
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_right_index = [0] * n
        max_right_index[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            max_right_index[i] = (
                i
                if num_str[i] > num_str[max_right_index[i + 1]]
                else max_right_index[i + 1]
            )
        for i in range(n):
            if num_str[i] < num_str[max_right_index[i]]:
                num_str[i], num_str[max_right_index[i]] = (
                    num_str[max_right_index[i]],
                    num_str[i],
                )
                return int("".join(num_str))
        return num


# Best / Most Optimal Solution
class Solution2:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        total_digits = len(digits)
        digits2indices = dict()
        for idx, digit in enumerate(digits):
            if digit not in digits2indices.keys():
                digits2indices.update({digit: []})
            digits2indices[digit].append(idx)
        digits2indices = dict(sorted(digits2indices.items(), reverse=True))
        current_idx = 0
        for digit, indices in digits2indices.items():
            for idx in indices[::-1]:
                while current_idx < total_digits - 1 and current_idx <= idx:
                    if digits[current_idx] < digits[idx]:
                        digits[current_idx], digits[idx] = (
                            digits[idx],
                            digits[current_idx],
                        )
                        return int("".join(digits))
                    if digits[current_idx] == digits[idx]:
                        current_idx += 1
                        continue
                if current_idx == total_digits - 1:
                    return int("".join(digits))
