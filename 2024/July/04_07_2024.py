from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        if not head:
            return head
        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            temp = temp.next
        head.val = sum
        head.next = self.mergeNodes(temp)
        return head

# Best / Most Optimal Solution
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = head
        curr = curr.next
        sum = 0
        while curr:
            if curr.val == 0:
                dummy = dummy.next
                dummy.val = sum
                sum = 0
            else:
                sum += curr.val
            curr = curr.next
        dummy.next = None
        return head.next
