import math
from typing import List


# My Solution
class Solution:
    def primeSubOperation(self, nums):
        max_element = max(nums)
        sieve = [1] * (max_element + 1)
        sieve[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if sieve[i] == 1:
                for j in range(i * i, max_element + 1, i):
                    sieve[j] = 0
        curr_value = 1
        i = 0
        while i < len(nums):
            difference = nums[i] - curr_value
            if difference < 0:
                return False
            if sieve[difference] or difference == 0:
                i += 1
                curr_value += 1
            else:
                curr_value += 1
        return True


# Best / Most Optimal Solution\
class Solution2:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Find all primes < 1000
        primes = {
            2,
            3,
            5,
            7,
            521,
            11,
            523,
            13,
            17,
            19,
            23,
            29,
            541,
            31,
            547,
            37,
            41,
            43,
            557,
            47,
            563,
            53,
            569,
            59,
            571,
            61,
            577,
            67,
            71,
            73,
            587,
            79,
            593,
            83,
            599,
            89,
            601,
            607,
            97,
            101,
            613,
            103,
            617,
            107,
            619,
            109,
            113,
            631,
            127,
            641,
            131,
            643,
            647,
            137,
            139,
            653,
            659,
            149,
            661,
            151,
            157,
            673,
            163,
            677,
            167,
            683,
            173,
            179,
            691,
            181,
            701,
            191,
            193,
            197,
            709,
            199,
            719,
            211,
            727,
            733,
            223,
            227,
            739,
            229,
            743,
            233,
            239,
            751,
            241,
            757,
            761,
            251,
            257,
            769,
            773,
            263,
            269,
            271,
            787,
            277,
            281,
            283,
            797,
            293,
            809,
            811,
            307,
            821,
            311,
            823,
            313,
            827,
            317,
            829,
            839,
            331,
            337,
            853,
            857,
            347,
            859,
            349,
            863,
            353,
            359,
            877,
            367,
            881,
            883,
            373,
            887,
            379,
            383,
            389,
            907,
            397,
            911,
            401,
            919,
            409,
            929,
            419,
            421,
            937,
            941,
            431,
            433,
            947,
            439,
            953,
            443,
            449,
            967,
            457,
            971,
            461,
            463,
            977,
            467,
            983,
            479,
            991,
            997,
            487,
            491,
            499,
            503,
            509,
        }
        curr = 0
        for num in nums:
            flag = False
            for i in range(num - curr - 1, -1, -1):
                if (i in primes or i == 0) and num - i > curr:
                    curr = num - i
                    flag = True
                    break
            if not flag:
                return False
        return True
