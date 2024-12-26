from collections import Counter
from heapq import heapify, heappop, heappush

# My Solution
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(max_heap)
        result = []
        while max_heap:
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            result.append(char * use)
            if count > use and max_heap:
                next_char_neg, next_count = heappop(max_heap)
                result.append(chr(-next_char_neg))
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, count - use))
        return "".join(result)
    
# Best / Most Optimal Solution
class Solution2:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = Counter(s)
        sorted_chars = sorted(chars.items(), reverse=True)
        ans = []
        while sorted_chars:
            char, freq = sorted_chars[0]
            if freq <= repeatLimit:
                ans.append(char * freq)
                sorted_chars.pop(0)
            else:
                ans.append(char * repeatLimit)
                sorted_chars[0] = (char, freq - repeatLimit)
                if len(sorted_chars) > 1:
                    next_char, next_freq = sorted_chars[1]
                    ans.append(next_char)
                    if next_freq == 1:
                        sorted_chars.pop(1)
                    else:
                        sorted_chars[1] = (next_char, next_freq - 1)
                else:
                    break
        return ''.join(ans)
