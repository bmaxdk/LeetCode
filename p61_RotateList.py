# 61. Rotate List

# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        old_tail = head
        size = 0
        
        while old_tail:
            size+=1
            if old_tail.next is None:
                break
            old_tail = old_tail.next

        if size == 0 or size ==1 or k==0:
            return head
        
        # index = (size+k)%size
        index = (size-k%size-1)#<--------
        # (n - k % n - 1)
        new_tail = head
        for _ in range(index):
            new_tail = new_tail.next
        
        new_head = new_tail.next if new_tail.next else head
        # new_head = new_head.next
        
        old_tail.next = head
        new_tail.next = None
        
        return new_head