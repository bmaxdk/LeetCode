# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         listA = headA
#         listB = headB
#         if listA == listB or listA is None or listB is None:
#             return 
#         iA = 0
#         cycle = 0
#         iB = 0
#         while listA != listB:
#             iA+=1
#             iB+=1
#             listA = listA.next
#             listB = listB.next
#             if listA is None:
#                 #need to switch to B
#                 listA = headB
#                 iA = 0
#                 cycle +=1
#             if listB is None:
#                 #need to switch to A
#                 listB = headA
#                 iB = 0
#                 cycle +=1
#             if cycle == 3:
#                 return 
#         if listA == None and listB == None:
#             return 
#         print("skipA = ", iB)
#         print("skipB = ", iA)
#         return listA



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listA = headA
        listB = headB
        # if listA == listB or listA is None or listB is None:
        #     return 
        # iA = 0
        # cycle = 0
        # iB = 0
        while listA != listB:
            listA = headB if listA is None else listA.next
            listB = headA if listB is None else listB.next
        return listA