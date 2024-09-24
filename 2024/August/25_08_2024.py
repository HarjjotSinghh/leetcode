from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def postOrder(self,root,answerList):

        if root == None:
            return answerList
        else:
            self.postOrder(root.left, answerList)
            self.postOrder(root.right, answerList)
            answerList.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.postOrder(root, answerList)

        return answerList

# Best / Most Optimal Solution
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result += [root.val]
        return result
