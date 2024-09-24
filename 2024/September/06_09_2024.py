from typing import List, Optional
import sys
from json import loads, dumps

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        values_to_remove = set(nums)
        while head and head.val in values_to_remove:
            head = head.next
        if not head:
            return None
        current = head
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Best / Most Optimal Solution
class Solution2:
    def modifiedList(self, excludeValues: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        exclude_set = set(excludeValues)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val in exclude_set:
                curr.next = curr.next.next  
            else:
                curr = curr.next  
        return dummy.next
def list_to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
def main():
    inputs = map(loads, sys.stdin)
    results = []
    for excludeValues in inputs:
        head_list = next(inputs)
        head = list_to_linked_list(head_list)
        filtered_head = Solution().modifiedList(excludeValues, head)
        results.append(linked_list_to_list(filtered_head))
    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)
if __name__ == "__main__":
    main()
    sys.exit(0)
