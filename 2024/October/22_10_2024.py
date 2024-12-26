from collections import deque
import heapq
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)
        while bfs_queue:
            size = len(bfs_queue)
            sum_val = 0
            for _ in range(size):
                popped_node = bfs_queue.popleft()
                sum_val += popped_node.val
                if popped_node.left is not None:
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None:
                    bfs_queue.append(popped_node.right)
            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                heapq.heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]


# Best / Most Optimal Solution
class Solution2:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels_sum = []

        def BFS(root):
            nonlocal levels_sum
            queue = deque([root])
            while queue:
                level_sum = 0
                queue_size = len(queue)
                for _ in range(queue_size):
                    node = queue.popleft()
                    level_sum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                levels_sum.append(level_sum)

        BFS(root)
        if len(levels_sum) < k:
            return -1
        levels_sum.sort(reverse=True)
        return levels_sum[k - 1]
