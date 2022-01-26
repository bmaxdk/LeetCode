# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Done
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        rev = None
        while curr:
            temp = curr
            curr = curr.next
            temp.next = rev
            rev = temp
        return rev
        

# # print current list val
# # 1->2->3 curr
# # to
# # 3->2->1 prev

# curr = head
# rev = None
# while curr:
# 	temp = curr
# 	curr = curr.next #
# 	temp.next = rev
# 	# print(rev.val)
# 	rev = temp
# 	# print(rev.val)
# 	# curr = curr.next
# 	# print(temp.val)


# Read!! bottom!!!!!
"""
aa = ListNode(3)
aa.next = ListNode(2)


# print(aa.val)
# print(aa.next.val)
a= aa
print("here a is 3->2")
print(a.val)
print(a.next.val)

temp = a
temp.next = None

print("issue here!")
print(a.val)
print("as it shows it's not 3->2 anymore")
print(a.next)

print("therefore, a.next also affects when assign temp")
"""
"""

aa = ListNode(3)
aa.next = ListNode(2)


# print(aa.val)
# print(aa.next.val)
a= aa
print("here a is 3->2")
print(a.val)
print(a.next.val)

temp = a
a.next = a.next
temp.next = None

print(a.val)
print(aa.next.val)
print("which it show error up here, all the aa linked list will effect!! Therefore, keep it mind!")
"""

# # while listT:
# # 	print(listT.val)
# # 	listT= listT.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         



