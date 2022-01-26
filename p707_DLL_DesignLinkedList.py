# 707. Design Linked List
# https://leetcode.com/problems/design-linked-list/
# DLL


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0) #
        self.head.next = self.tail #
        self.tail.prev = self.head #

    def get(self, index: int) -> int:

        if self.size < 0 or index >= self.size: ##<<<-----
            return -1
        
        if self.size-index > index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        # self.addAtIndex(0, val)
        self.size+=1
        addHead = ListNode(val)
        pred, succ = self.head, self.head.next
        addHead.prev =pred
        addHead.next = succ
        pred.next = addHead
        succ.prev = addHead

    def addAtTail(self, val: int) -> None:
        # self.addAtIndex(self.size, val)
        self.size+=1
        addTail = ListNode(val)
        pred, succ = self.tail.prev, self.tail
        addTail.prev = pred
        addTail.next = succ
        pred.next = addTail
        succ.prev = addTail

    def addAtIndex(self, index: int, val: int) -> None:
        if index <0:
            index = 0
        if index > self.size:
            return

        if self.size-index > index:
            pred = self.head
            for _ in range(index):
                pred=pred.next

            succ = pred.next

        else:
            succ = self.tail
            for _ in range(self.size-index):
                succ=succ.prev
            pred = succ.prev

        self.size +=1
        add = ListNode(val)
        add.next = succ
        add.prev = pred
        pred.next = add
        succ.prev = add
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  ##<<<-----
            return
        
        if self.size-index > index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next

        else:
            succ = self.tail
            for _ in range(self.size-index-1): ##<-----
                succ = succ.prev
            pred = succ.prev.prev

        pred.next = succ
        succ.prev = pred
        self.size -=1

        
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev #

# ------------------------------------------------------------------------
# Singly Linked List

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Singly Linked List
# class MyLinkedList:

#     def __init__(self):
#         self.size = 0
#         self.head = ListNode(0)

#     def get(self, index: int) -> int:
#         if self.size < 0 or index >= self.size: ##<<<-----
#             return -1
#         curr = self.head
#         for _ in range(index+1):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0, val)

#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size, val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index <0:
#             index = 0
#         if index > self.size:
#             return
#         self.size +=1
#         prev = self.head
#         for _ in range(index):
#             prev = prev.next
#         add = ListNode(val)
#         add.next = prev.next
#         prev.next = add
        
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:  ##<<<-----
#             return
        
#         self.size -=1
#         prev = self.head
#         for _ in range(index):
#             prev = prev.next
#         prev.next = prev.next.next
        
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




# class MyLinkedList:

#     def __init__(self):
#         self.size = 0
#         self.head = ListNode(0)

#     def get(self, index: int) -> int:
#         if self.size < 0 or index >= self.size: ##<<<-----
#             return -1
#         curr = self.head
#         for _ in range(index+1):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0, val)

#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size, val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index <0:
#             index = 0
#         if index > self.size:
#             return
#         self.size +=1
#         pred = self.head
#         for _ in range(index):
#             pred = pred.next
#         add = ListNode(val)
#         add.next = pred.next
#         pred.next = add
        
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:  ##<<<-----
#             return
        
#         self.size -=1
#         pred = self.head
#         for _ in range(index):
#             pred = pred.next
#         pred.next = pred.next.next
        
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
        

# # # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# # # param_1 = obj.get(index)
# # # obj.addAtHead(val)
# # # obj.addAtTail(val)
# # # obj.addAtIndex(index,val)
# # # obj.deleteAtIndex(index)
# obj.addAtIndex(0,6)
# print(obj.get(0))
# print(obj.size)