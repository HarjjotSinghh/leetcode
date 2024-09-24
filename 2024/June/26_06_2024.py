import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self.right_rotate(current, current.right)
            else:
                current = current.right
        node_count = 0
        current = vine_head.right
        while current:
            node_count += 1
            current = current.right
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self.make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self.make_rotations(vine_head, m)
        balanced_root = vine_head.right
        vine_head = None
        return balanced_root
    def right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        parent.right = tmp
    def left_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        parent.right = tmp
    def make_rotations(self, vine_head: TreeNode, count: int):
        current = vine_head
        for _ in range(count):
            tmp = current.right
            self.left_rotate(current, tmp)
            current = current.right

# Best / Most Optimal Solution          
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inorder(root, nodes)
        return self.buildBST(nodes, 0, len(nodes)-1)
    def inorder(self, root: TreeNode, nodes):
        if not root:
            return 
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)
    def buildBST(self, nodes, left, right) -> TreeNode:
        if left > right:
            return None
        mid = (left + right)//2
        node = nodes[mid]
        node.left = self.buildBST(nodes, left, mid-1)
        node.right = self.buildBST(nodes, mid+1, right)
        return node
