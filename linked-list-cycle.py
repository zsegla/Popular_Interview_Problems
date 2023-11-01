# https://leetcode.com/problems/linked-list-cycle/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        
        return False
        
