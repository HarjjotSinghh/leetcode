from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        result_map = {}
        height_cache = {}

        def _height(node):
            if not node:
                return -1
            if node in height_cache:
                return height_cache[node]
            h = 1 + max(_height(node.left), _height(node.right))
            height_cache[node] = h
            return h

        def _dfs(node, depth, max_val):
            if not node:
                return
            result_map[node.val] = max_val
            _dfs(
                node.left,
                depth + 1,
                max(max_val, depth + 1 + _height(node.right)),
            )
            _dfs(
                node.right,
                depth + 1,
                max(max_val, depth + 1 + _height(node.left)),
            )

        _dfs(root, 0, 0)
        return [result_map[q] for q in queries]


# Best / Most Optimal Solution
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = dict()
        max_height = float("-inf")

        def set_heights(root):
            nonlocal max_height, heights
            if not root:
                return -1
            left_height, right_height = set_heights(root.left), set_heights(root.right)
            heights[root.val] = max(left_height, right_height) + 1
            max_height = max(max_height, heights[root.val])
            return heights[root.val]

        set_heights(root)
        cache = dict()

        def set_best_height_without_node(root, depth, best_height_without_node):
            if not root:
                return
            cache[root.val] = best_height_without_node
            left_height = heights[root.left.val] if root.left else -1
            right_height = heights[root.right.val] if root.right else -1
            if left_height > right_height:
                best_height_without_node = max(
                    best_height_without_node, right_height + depth + 1
                )
                set_best_height_without_node(
                    root.left, depth + 1, best_height_without_node
                )
            else:
                best_height_without_node = max(
                    best_height_without_node, left_height + depth + 1
                )
                set_best_height_without_node(
                    root.right, depth + 1, best_height_without_node
                )

            return

        set_best_height_without_node(root, 0, 0)
        ans = []
        for query in queries:
            if query in cache:
                ans.append(cache[query])
            else:
                ans.append(max_height)
        return ans
