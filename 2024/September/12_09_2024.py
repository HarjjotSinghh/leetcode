from typing import List

# My Solution
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        consistent_count = 0
        for word in words:
            if all(char in allowed_chars for char in word):
                consistent_count += 1
        return consistent_count

# Best / Most Optimal Solution
class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        occur = [False] * 26
        count = 0
        for c in allowed:
            occur[ord(c) - ord('a')] = True
        for word in words:
            if self.check(word, occur):
                count += 1
        return count
    def check(self, word: str, occur: List[bool]) -> bool:
        for c in word:
            if not occur[ord(c) - ord('a')]:
                return False
        return True
def harjotmain():
    input_data = sys.stdin.read().strip().split('\n')
    results = []
    i = 0
    while i < len(input_data):
        allowed = json.loads(input_data[i])
        words = json.loads(input_data[i + 1])
        result = Solution().countConsistentStrings(allowed, words)
        results.append(result)
        i += 2
    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
if __name__ == "__main__":
    harjotmain()
    exit(0)
