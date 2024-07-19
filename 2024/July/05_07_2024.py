from typing import List, Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left = head
        mid = head.next
        if not mid or not mid.next:
            return [-1, -1]
        right = mid.next
        idx = 2
        idxs = []
        while right:
            if (mid.val > left.val and mid.val > right.val) or (mid.val < left.val and mid.val < right.val):
                idxs.append(idx)
            left = mid
            mid = right
            right = right.next
            idx += 1
        if len(idxs) < 2:
            return [-1, -1]
        min_distance = float('inf')
        max_distance = idxs[-1] - idxs[0]
        for i in range(1, len(idxs)):
            min_distance = min(min_distance, idxs[i] - idxs[i - 1])
        return [min_distance, max_distance]

# Best / Most Optimal Solution
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mind = math.inf
        prevc = None
        currc = None
        prev = head
        cur = head.next
        nex = cur.next
        firstc = None
        i = 1
        while(nex):
            if (nex.val > cur.val and prev.val > cur.val) or (nex.val < cur.val and prev.val < cur.val):
                if prevc == None:
                    firstc = i
                    prevc = i
                    currc = i
                else:
                    prevc = currc
                    currc = i
                    mind = min(mind,currc-prevc)
            i += 1
            prev = cur
            cur = nex
            nex = cur.next
        if mind == math.inf:
            return [-1,-1]
        return [mind,currc-firstc]
