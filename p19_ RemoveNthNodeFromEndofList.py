# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        #1. Think as connect sentinel to head
        sentinel = ListNode(0)
        sentinel.next = head
        
        #2. set prev and curr
        prev, curr = sentinel, head
        
        #get Length of head:
        length = 0
        while head:
            length+=1
            head =head.next
#             
        i = 0
        while curr:
            i += 1
            if i == length-n+1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return sentinel.next




''' 
Here is not optimize for memory

Runtime: 32 ms, 
faster than 79.31% of Python3 online submissions 
for Remove Nth Node From End of List.

Memory Usage: 14.3 MB, 
less than 49.92% of Python3 online submissions 
for Remove Nth Node From End of List.
'''