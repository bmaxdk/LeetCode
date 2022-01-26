# https://leetcode.com/problems/remove-linked-list-elements/
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        i = 0
        prev, curr = sentinel, head
        while curr:
            # print(i)
            # i+=1
            if curr.val == val:
                # print(curr.val)
                prev.next = curr.next
            
            else: 
                # print(curr.val)
                prev = curr
            curr = curr.next
        
        return sentinel.next



# head = [1,2,6,3,4,5,6]

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next = ListNode(6)
# print(b.val)
# print(b.next.val)
# print(b.next.next.val)



# a = Solution()
# a.removeElements(head,6)
# print(a)
#by HC
class Remove_element:
    def removeList(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode
        sentinel.next = head

        prev = sentinel
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next

            else:
                prev = curr

            curr = curr.next
        return sentinel.next

a = Remove_element()
a.removeList(head, 6)

# print('here')

sentinel = ListNode(0)
sentinel.next = head
prev, curr = sentinel, head
while curr:
    # print(curr.val)
    prev=curr
    curr = curr.next

# 