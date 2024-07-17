from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if not root:
            return []
        to_delete_set = set(to_delete)
        forest = []
        nodes_queue = deque([root])
        while nodes_queue:
            current_node = nodes_queue.popleft()
            if current_node.left:
                nodes_queue.append(current_node.left)
                if current_node.left.val in to_delete_set:
                    current_node.left = None
            if current_node.right:
                nodes_queue.append(current_node.right)
                if current_node.right.val in to_delete_set:
                    current_node.right = None
            if current_node.val in to_delete_set:
                if current_node.left:
                    forest.append(current_node.left)
                if current_node.right:
                    forest.append(current_node.right)
        if root.val not in to_delete_set:
            forest.append(root)
        return forest
    
# Best / Most Optimal Solution
class Solution:
    def helper(self, node, parent):
        if node is None:
            return
        node.parent = parent
        if node.val in self.toDel:
            self.nodes.pop(node.val)
            if parent:
                if parent.left and parent.left.val == node.val:
                    parent.left = None
                if parent.right and parent.right.val == node.val:
                    parent.right = None
            self.helper(node.left, None)
            self.helper(node.right, None)
            return
        self.helper(node.left, node)
        self.helper(node.right, node)
    def traverse(self, node, parent):
        if node is None:
            return
        self.nodes[node.val] = node
        node.parent = parent
        self.traverse(node.left, node)
        self.traverse(node.right, node)
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.toDel = set(to_delete)
        self.nodes = {}
        self.traverse(root, None)
        self.helper(root, None)
        return [node for node in self.nodes.values() if not node.parent]
