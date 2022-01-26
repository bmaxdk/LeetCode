# approach2
# https://leetcode.com/problems/linked-list-cycle/
# class ListNode:
# 	def __init__(self, val=0, next=None):
# 		self.val = val
# 		self.next = next

# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(3)
# head.next.next.next.next.next = ListNode(4)
# head.next.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next.next = ListNode(6)

# print(head == head)

# a =head.next.next.next
# b =head.next.next.next.next.next.next.next 
# print(a==b)

# c = head
# d = head

# print(c == d)

# e = head.next.next.next

# print(a==e)

# a=ListNode(0)
# b=ListNode(0)
# print(a==b)
# print(a)

# print(c)
# print(d)
# a=3
# b=a
# b+=1
# print(a)
# print(b)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
       
    
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
            
# # sol   
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head == None:
#             return False
#         slow = head
#         fast = head.next
        
#         while slow != fast:
#             if fast == None or fast.next == None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True
        