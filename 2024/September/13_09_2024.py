import json
import sys

# My Solution
class Solution:
    def xorQueries(self, arr, queries):
        result = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])
        return result

# Best / Most Optimal Solution
class Solution2:
    def xorQueries(self, arr, queries):
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ arr[i]
        xor = []
        for l, r in queries:
            if l > 0:
                xor.append(arr[r] ^ arr[l-1])
            else:
                xor.append(arr[r])
        return xor
def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    num_test_cases = len(lines) // 2
    results = []
    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        queries = json.loads(lines[i*2 + 1])
        result = Solution().xorQueries(arr, queries)
        results.append(json.dumps(result, separators=(',', ':')))
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    main()
    exit(0)
