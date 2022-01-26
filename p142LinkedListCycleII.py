
# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

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
# print('c==d')
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
# set_a = {c, d, a}
# print("len(set_a)")
# print(len(set_a))
# print(c==d)
# set_a.add(e)
# print(len(set_a))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        if head == None or fast.next == None or fast.next.next == None:
            print("There is no cycle in the linked list.")
            return 
        fast = fast.next.next
        slow = slow.next
        while fast != slow:
            if fast.next == None or fast.next.next == None:
                print("There is no cycle in the linked list.")
                return 
            slow = slow.next
            fast = fast.next.next
        
        i = 0
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
            i+=1
        print("tail connects to node index {}".format(i))    
        return fast