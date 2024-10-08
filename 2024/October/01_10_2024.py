from typing import List
import sys
import json

# My Solution
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted(arr, key=lambda x: (k + x % k) % k)
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] % k != 0:
                break
            if arr[start + 1] % k != 0:
                return False
            start = start + 2
        while start < end:
            if (arr[start] + arr[end]) % k != 0:
                return False
            start += 1
            end -= 1
        return True

# Best / Most Optimal Solution
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for num in arr:
            freq[(num % k + k) % k] += 1
        if freq[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False
        return True
def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines) // 2
    results = []
    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        k = int(lines[i*2 + 1])
        result = Solution().canArrange(arr, k)
        results.append(str(result).lower()) 
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    main()
    exit(0)
