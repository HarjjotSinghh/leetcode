from typing import List
from collections import defaultdict
from bisect import bisect_right


# My Solution
class Solution:
    def maximumBeauty(self, items, queries):
        ans = [0] * len(queries)
        items.sort(key=lambda x: x[0])
        queries_with_indices = [[queries[i], i] for i in range(len(queries))]
        queries_with_indices.sort(key=lambda x: x[0])
        item_index = 0
        max_beauty = 0
        for i in range(len(queries)):
            query = queries_with_indices[i][0]
            original_index = queries_with_indices[i][1]
            while item_index < len(items) and items[item_index][0] <= query:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1
            ans[original_index] = max_beauty
        return ans


# Best / Most Optimal Solution
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maxb = defaultdict(int)
        minb1 = 0
        items.sort(key=lambda x: x[0])
        pp = None
        maxb[items[0][0]] = items[0][1]
        for i1 in range(1, len(items)):
            i = items[i1]
            maxb[i[0]] = max(maxb[items[i1 - 1][0]], i[1])
        k = list(maxb.keys())
        ans = []
        for q in queries:
            if maxb[q] == 0:
                qq = bisect_right(k, q)
                if qq > 0:
                    maxb[q] = maxb[k[qq - 1]]
                else:
                    maxb[q] = 0
            ans.append(maxb[q])
        return ans
