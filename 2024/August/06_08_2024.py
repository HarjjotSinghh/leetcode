from collections import Counter
import heapq

# My Solution
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency_map = Counter(word)
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)
        total_pushes = 0
        index = 0
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (
                -heapq.heappop(frequency_queue)
            )
            index += 1
        return total_pushes
    
# Best / Most Optimal Solution
class Solution2:
    def minimumPushes(self, word: str) -> int:
        l=[0]*(32)
        for i in range(26):
            l[i]=word.count(chr(97+i))
        l.sort(reverse=True)
        res=0
        for i in range(4):
            for j in range(8):
                res+=(i+1)*l[8*i+j]
        return res
