# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        newList = result
        while l1 and l2:
            if l1.val < l2.val:
                newList.next = l1
                l1 = l1.next
            else:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        newList.next = l1 or l2
        return result.next
    
    