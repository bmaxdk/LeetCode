# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        l_current = l
        d = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            c = a + b + d
            d = 0
            if c >= 10:
                c = c - 10
                d = 1
            l_current.next = ListNode(c)
            l_current = l_current.next

        if d > 0:
            l_current.next = ListNode(d)
        return l.next
