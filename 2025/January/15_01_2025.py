# My Solution
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0
        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31
        while set_bits_count < target_set_bits_count:
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1
        return result

    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)


# Best / Most Optimal Solution
class Solution2:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")
        if bits1 == bits2:
            return num1
        if bits1 > bits2:
            r = num1
            remove = bits1 - bits2
            x = 1
            while remove > 0:
                if r & x > 0:
                    r ^= x
                    remove -= 1
                x <<= 1
            return r
        if bits1 < bits2:
            r = num1
            add = bits2 - bits1
            x = 1
            while add > 0:
                if r & x == 0:
                    r |= x
                    add -= 1
                x <<= 1
            return r
