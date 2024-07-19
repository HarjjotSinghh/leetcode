from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution        
class Solution:
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        for description in descriptions:
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]
            children.add(child_value)
        for node in node_map.values():
            if node.val not in children:
                return node
        return None

# Best / Most Optimal Solution
class Solution2:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        child = set()
        for p, c, l in descriptions:
            child.add(c)
            if p in d:
                p = d[p]
            else:
                d[p] = TreeNode(p)
                p = d[p]
            if c in d:
                c = d[c]
            else:
                d[c] = TreeNode(c)
                c = d[c]
            if l:
                p.left = c
            else:
                p.right = c
        for p, _, _ in descriptions:
            if p not in child: return d[p]
        return None
