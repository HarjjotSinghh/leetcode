# My Solution
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        position_in_section = k & -k
        is_in_inverted_part = ((k // position_in_section) >> 1 & 1) == 1
        original_bit_is_one = (k & 1) == 0
        if is_in_inverted_part:
            return "0" if original_bit_is_one else "1"
        else:
            return "1" if original_bit_is_one else "0"


# Best / Most Optimal Solution
class Solution2:
    def findKthBit(self, n: int, k: int) -> str:
        def findKthBitRecursive(n, k):
            if n == 1:
                return "0"
            length_of_sn_minus_1 = (1 << (n - 1)) - 1
            middle = length_of_sn_minus_1 + 1
            if k == middle:
                return "1"
            elif k < middle:
                return findKthBitRecursive(n - 1, k)
            else:
                corresponding_position = 2 * length_of_sn_minus_1 + 2 - k
                bit = findKthBitRecursive(n - 1, corresponding_position)
                return "0" if bit == "1" else "1"

        return findKthBitRecursive(n, k)
