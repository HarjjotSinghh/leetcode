
# My Solution
class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            if ch == "[":
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2

# Best / Most Optimal Solution
class Solution:
  def minSwaps(self, s: str) -> int:
    unmatched = 0
    for c in s:
      if c == '[':
        unmatched += 1
      elif unmatched > 0:
        unmatched -= 1
    return (unmatched + 1) // 2
