from typing import List

# My Solution
class Solution:
    def _sieve(self, upper_limit):
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False
        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve
    def closestPrimes(self, left, right):
        sieve_array = self._sieve(right)
        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]
        if len(prime_numbers) < 2:
            return -1, -1
        min_difference = float("inf")
        closest_pair = (-1, -1)
        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]
        return closest_pair

# Best / Most Optimal Solution
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right - left < 1:
            return [-1, -1]
        left = max(2, left)
        if left == 2 and right >= 3:
            return [2, 3]
        if left & 1 == 0:
            left += 1
        prev_prime = -1
        min_diff = float('inf')
        res = [-1, -1]
        def is_composite_witness(n: int, witness: int, d: int, s: int) -> bool:
            x = pow(witness, d, n)
            if x == 1 or x == n - 1:
                return False
            for _ in range(1, s):
                x = pow(x, 2, n)
                if x == n - 1:
                    return False
            return True
        def miller_rabin(n: int) -> bool:
            if n < 2:
                return False
            small_primes = [2, 3]
            for p in small_primes:
                if n == p:
                    return True
                if n % p == 0:
                    return False
            s = 0
            d = n - 1
            while d & 1 == 0:
                d >>= 1
                s += 1
            for witness in small_primes:
                if is_composite_witness(n, witness, d, s):
                    return False
            return True
        for candidate in range(left, right + 1, 2):
            if not miller_rabin(candidate):
                continue
            if prev_prime != -1:
                diff = candidate - prev_prime
                if diff == 2:
                    return [prev_prime, candidate]
                if diff < min_diff:
                    min_diff = diff
                    res = [prev_prime, candidate]
            prev_prime = candidate
        return res
