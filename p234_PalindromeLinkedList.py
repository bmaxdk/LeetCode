# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #initial condition
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return True if head.val == head.next.val else False
#         if head.next.next.next is None:
#             return True if head.val == head.next.next.val else False
        
        
        checkP = []
        fast = head
        slow = head
        checkP.append(slow.val)
        count = 0
        # collect checkP
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            checkP.append(slow.val)
            if fast.next is None:
                count =1
                
        size = len(checkP)-count
        slow = slow.next
        while slow:
            size -=1
            if slow.val != checkP[size]:
                return False
            slow = slow.next
        return True
            
#             1->2->3->2->1
#                s  f
#                   s     f
#             f        s   
            
            
#             1->2->3->4->4->3->2->1
#                s  f  
#                   s     f
#                      s-       f!
#             f           s
            
# #             reset f and s
#                2->3->3->2
#                   s- f!
                     
            
                   
# # [1 0 0]
# x = ListNode(1)
# x.next = ListNode(0)
# x.next.next = ListNode(0)

# test = Solution()
# print(test.isPalindrome(x))