from typing import List
from collections import deque
from heapq import heappop, heappush


# My Solution
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(str, i, j):
            ls = list(str)
            ls[i], ls[j] = ls[j], ls[i]
            return "".join(ls)

        target = "123450"
        start = "".join(str(cell) for row in board for cell in row)
        queue = deque()
        queue.append([start, start.index("0"), 0])
        visited = set(start)
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        while queue:
            current_state, pos, steps = queue.popleft()
            if current_state == target:
                return steps
            for neighor in neighbors[pos]:
                new_state = swap(current_state, pos, neighor)
                if new_state not in visited:
                    queue.append([new_state, neighor, steps + 1])
                    visited.add(new_state)
        return -1


# Best / Most Optimal Solution
class Solution2:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = 2, 3
        seq = []
        start, end = "", "123450"
        for i in range(m):
            for j in range(n):
                if board[i][j] != 0:
                    seq.append(board[i][j])
                start += str(board[i][j])

        def check(seq):
            n = len(seq)
            cnt = sum(seq[i] > seq[j] for i in range(n) for j in range(i, n))
            return cnt % 2 == 0

        def f(s):
            ans = 0
            for i in range(m * n):
                if s[i] != "0":
                    num = ord(s[i]) - ord("1")
                    ans += abs(i // n - num // n) + abs(i % n - num % n)
            return ans

        if not check(seq):
            return -1
        q = [(f(start), start)]
        dist = {start: 0}
        while q:
            _, state = heappop(q)
            if state == end:
                return dist[state]
            p1 = state.index("0")
            i, j = p1 // n, p1 % n
            s = list(state)
            for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    p2 = x * n + y
                    s[p1], s[p2] = s[p2], s[p1]
                    next = "".join(s)
                    s[p1], s[p2] = s[p2], s[p1]
                    if next not in dist or dist[next] > dist[state] + 1:
                        dist[next] = dist[state] + 1
                        heappush(q, (dist[next] + f(next), next))
        return -1
