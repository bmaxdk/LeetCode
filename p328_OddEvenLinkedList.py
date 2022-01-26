# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return
#         odd =head
#         evenHead = odd.next
#         even = evenHead
#         while odd:
#             if odd.next is None or even.next is None:
#                 odd.next = evenHead
#                 return head
#             odd.next = even.next
#             odd = odd.next
#             even.next =odd.next
#             even = even.next
            
#         odd.next = evenHead
#         return head
    
    
# updated<--------------------------Use this way
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        odd =head
        evenHead = head.next
        even = evenHead
        while even and even.next:
            # if odd.next is None or even.next is None:
            #     odd.next = evenHead
            #     return head
            odd.next = even.next
            odd = odd.next
            even.next =odd.next
            even = even.next
            
        odd.next = evenHead
        return head


    
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return
#         odd =head
#         even = ListNode(0)
#         even.next = odd.next
#         evenHead = even.next
#         while odd:
#             if odd.next is None or evenHead.next is None:
#                 odd.next = even.next
#                 return head
#             odd.next = odd.next.next
#             odd = odd.next
#             evenHead.next = evenHead.next.next
#             evenHead = evenHead.next
            
#         #     odd.next = even.next
#         #     even.next = odd.next
#         #     odd = odd.next
#         #     evenHead = even.next
#         #     even = odd.next
#         # odd.next = even
#         odd.next = even.next
#         return head





# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return
#         odd =head
#         even = ListNode(0)
#         even.next = odd.next
#         evenHead = even.next
#         while odd:
#             if odd.next is None or evenHead.next is None:
#                 odd.next = even.next
#                 return head
#             odd.next = odd.next.next
#             odd = odd.next
#             evenHead.next = evenHead.next.next
#             evenHead = evenHead.next
            
#         #     odd.next = even.next
#         #     even.next = odd.next
#         #     odd = odd.next
#         #     evenHead = even.next
#         #     even = odd.next
#         # odd.next = even
#         odd.next = even.next
#         return head
    