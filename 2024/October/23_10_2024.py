from collections import deque


# My Solution
class Solution:
    def __init__(self):
        self.level_sums = [0] * 100000

    def replaceValueInTree(self, root):
        self._calculate_level_sum(root, 0)
        self.replace_value_in_tree_internal(root, 0, 0)
        return root

    def _calculate_level_sum(self, node, level):
        if node is None:
            return
        self.level_sums[level] += node.val
        self._calculate_level_sum(node.left, level + 1)
        self._calculate_level_sum(node.right, level + 1)

    def replace_value_in_tree_internal(self, node, sibling_sum, level):
        if node is None:
            return
        left_child_val = 0 if node.left is None else node.left.val
        right_child_val = 0 if node.right is None else node.right.val

        if level == 0 or level == 1:
            node.val = 0
        else:
            node.val = self.level_sums[level] - node.val - sibling_sum
        self.replace_value_in_tree_internal(node.left, right_child_val, level + 1)
        self.replace_value_in_tree_internal(node.right, left_child_val, level + 1)


# Best / Most Optimal Solution
class Solution2:
    def replaceValueInTree(self, root):
        if root is None:
            return root
        nodeQueue = deque()
        nodeQueue.append(root)
        previousLevelSum = root.val
        while nodeQueue:
            levelSize = len(nodeQueue)
            currentLevelSum = 0
            for _ in range(levelSize):
                currentNode = nodeQueue.popleft()
                currentNode.val = previousLevelSum - currentNode.val
                siblingSum = (
                    0 if currentNode.left is None else currentNode.left.val
                ) + (0 if currentNode.right is None else currentNode.right.val)

                if currentNode.left is not None:
                    currentLevelSum += currentNode.left.val
                    currentNode.left.val = siblingSum
                    nodeQueue.append(currentNode.left)
                if currentNode.right is not None:
                    currentLevelSum += currentNode.right.val
                    currentNode.right.val = siblingSum
                    nodeQueue.append(currentNode.right)
            previousLevelSum = currentLevelSum
        return root
