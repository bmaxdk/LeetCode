# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prod = head
        curr = prod.next
        while curr:
            if prod.val == curr.val:
                prod.next = curr.next
                curr = prod.next
                
            else:
                prod = prod.next
                curr = prod.next
        return head