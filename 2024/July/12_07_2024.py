from typing import Tuple

# My Solution
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, first: str, second: str, points: int) -> Tuple[str, int]:
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        if x > y:
            s, score_x = remove_pair(s, 'a', 'b', x)
            s, score_y = remove_pair(s, 'b', 'a', y)
        else:
            s, score_y = remove_pair(s, 'b', 'a', y)
            s, score_x = remove_pair(s, 'a', 'b', x)
        return score_x + score_y
    
# Best / Most Optimal Solution
class Solution2:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        letter_a = "a"
        if x < y:
            letter_a = "b"
            x, y = y, x
        total = 0
        dxy = x-y
        ab_count = a_count = b_count = 0
        for char in s:
            if char not in "ab":
                if b_count > a_count:
                    a_count, b_count = b_count, a_count
                if a_count > 0:
                    total += ab_count*dxy+b_count*y
                    ab_count = a_count = b_count = 0
            elif char == letter_a:
                a_count += 1
            else:
                b_count += 1
                if a_count > ab_count:
                    ab_count += 1
        total += ab_count*dxy+min(a_count, b_count)*y
        return total
