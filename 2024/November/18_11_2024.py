from typing import List


# My Solution
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0 for _ in range(len(code))]
        if k == 0:
            return result
        start, end, window_sum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            window_sum += code[i]
        for i in range(len(code)):
            result[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return result


# Best / Most Optimal Solution
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        arrlen = len(code)
        decryptCode = [0 for i in range(arrlen)]
        currSum = sum(code[: abs(k)])
        for i in range(arrlen):
            if k < 0:
                if i == 0:
                    decryptCode[abs(k)] = currSum
                else:
                    currSum = (
                        currSum
                        - code[(i - 1) % arrlen]
                        + code[(abs(k) + i - 1) % arrlen]
                    )
                    decryptCode[(abs(k) + i) % arrlen] = currSum
            else:
                if i == 0:
                    decryptCode[arrlen - 1] = currSum
                else:
                    currSum = (
                        currSum - code[(i - 1) % arrlen] + code[(k + i - 1) % arrlen]
                    )
                    decryptCode[i - 1] = currSum
        return decryptCode
