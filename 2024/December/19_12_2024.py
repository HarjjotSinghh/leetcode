from collections import deque

# My Solution
class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        chunks = 0
        max_element = 0
        for i in range(n):
            max_element = max(max_element, arr[i])
            if max_element == i:
                chunks += 1
        return chunks
    
# Best / Most Optimal Solution
class Solution2:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        stack = deque()
        for i in range(n):
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)
        return len(stack)
