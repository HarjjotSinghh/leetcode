from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        pattern = [head.val]
        prefix_table = [0]
        pattern_index = 0
        head = head.next
        while head:
            while pattern_index > 0 and head.val != pattern[pattern_index]:
                pattern_index = prefix_table[pattern_index - 1]
            pattern_index += 1 if head.val == pattern[pattern_index] else 0
            pattern.append(head.val)
            prefix_table.append(pattern_index)
            head = head.next
        return self._search_in_tree(root, 0, pattern, prefix_table)
    def _search_in_tree(
        self,
        node: Optional[TreeNode],
        pattern_index: int,
        pattern: List[int],
        prefix_table: List[int],
    ) -> bool:
        if not node:
            return False
        while pattern_index > 0 and node.val != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index - 1]
        pattern_index += 1 if node.val == pattern[pattern_index] else 0
        if pattern_index == len(pattern):
            return True
        return self._search_in_tree(
            node.left, pattern_index, pattern, prefix_table
        ) or self._search_in_tree(
            node.right, pattern_index, pattern, prefix_table
        )

# Best / Most Optimal Solution
class Solution:
    def check_next_node(self,head,root):
        checkLeft, checkRight = False, False
        if not head:
            return True
        if root.left and root.left.val == head.val:
            checkLeft = self.check_next_node(head.next,root.left)
        if root.right and root.right.val == head.val:
            checkRight = self.check_next_node(head.next,root.right)
        return checkLeft or checkRight
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == head.val:
            if self.check_next_node(head.next,root):
                return True
        checkLeft = self.isSubPath(head,root.left)
        checkRight = self.isSubPath(head,root.right)
        return checkLeft or checkRight
