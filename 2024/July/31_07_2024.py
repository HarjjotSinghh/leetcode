from typing import List
import math

# My Solution
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = books[0][1]
        for i in range(2, n + 1):
            remaining_shelf_width = shelfWidth - books[i - 1][0]
            max_height = books[i - 1][1]
            dp[i] = books[i - 1][1] + dp[i - 1]
            j = i - 1
            while j > 0 and remaining_shelf_width - books[j - 1][0] >= 0:
                max_height = max(max_height, books[j - 1][1])
                remaining_shelf_width -= books[j - 1][0]
                dp[i] = min(dp[i], max_height + dp[j - 1])
                j -= 1
        return dp[n]

# Best / Most Optimal Solution
class Solution2:
    def minHeightShelves(self, books: List[List   [int]], shelfWidth: int) -> int:
        return self.dfs(books, shelfWidth, 0, shelfWidth, 0, {})
    def bfs(self, books, shelf_width):
        queue = [(shelf_width - books[0][0], books[0][1], 0)]
        for b in range(1, len(books)):
            queue_size = len(queue)
            while queue_size > 0:
                queue_size -= 1
                current = queue.pop(0)
                if current[0] >= books[b][0]:
                    queue.append((current[0]-books[b][0], max(current[1], books[b][1]), current[2]))
                if current[0] < books[b][0] or books[b][1] > current[1]:
                    queue.append((shelf_width-books[b][0], books[b][1], current[2] + current[1]))
        min_height = math.inf
        for x in queue:
            min_height = min(min_height, x[1] + x[2])
        return min_height
    def dfs(self, books, shelf_width, row_height, width_remaining, j, memo):
        if j >= len(books):
            return row_height
        key =  str(j) + "," + str(width_remaining)
        if key in memo:  return memo[key]
        book = books[j]
        same_row, new_col = math.inf, math.inf
        if width_remaining >= book[0]:
            same_row = self.dfs(books, shelf_width, max(row_height, book[1]), \
                                width_remaining - book[0], j+1, memo)
        if width_remaining < book[0] or book[1] > row_height:
            new_col = self.dfs(books, shelf_width, book[1], \
                               shelf_width - book[0], j+1, memo) + row_height
        memo[key] = min(same_row, new_col)
        return memo[key]
