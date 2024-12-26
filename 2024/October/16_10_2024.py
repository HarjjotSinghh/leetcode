import heapq


# My Solution
class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))
        result = []
        while heap:
            count1, char1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, char2))
                heapq.heappush(heap, (count1, char1))
            else:
                result.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, char1))
        return "".join(result)


# Best / Most Optimal Solution
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxh = []
        if a:
            heapq.heappush(maxh, (-a, "a"))
        if b:
            heapq.heappush(maxh, (-b, "b"))
        if c:
            heapq.heappush(maxh, (-c, "c"))
        res = ""
        while maxh:
            f1, c1 = heapq.heappop(maxh)
            f1 *= -1
            if len(res) >= 2 and res[-1] == res[-2] == c1:
                if not maxh:
                    return res
                f2, c2 = heapq.heappop(maxh)
                f2 *= -1
                res += c2
                f2 -= 1
                if f2:
                    heapq.heappush(maxh, (-1 * f2, c2))
                heapq.heappush(maxh, (-1 * f1, c1))
                continue
            res += c1
            f1 -= 1
            if f1:
                heapq.heappush(maxh, (-1 * f1, c1))
        return res
