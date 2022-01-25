# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            swap = head.next
            head.next = swap.next
            swap.next = head
            head = swap
            if head.next.next:
                head.next.next = self.swapPairs(head.next.next)
        return head
