# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        
        if root:
            q.append(root)
            
        while len(q):
            addq = None
            for _ in range(len(q)):
                deq = q.popleft()
                
                if addq:
                    addq.next = deq
                
                if deq.left:
                    q.append(deq.left)
                if deq.right:
                    q.append(deq.right)

                addq = deq
        return root
    
    
# from collections import deque

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         q = deque()
#         res = []
#         if root:
#             q.append(root)
#         while len(q):
#             # visit = []
            
#             addq = None
#             for _ in range(len(q)):
                
#                 deq = q.popleft()
#                 # visit.append(deq.val)
#                 if addq:
#                     addq.next = deq
                
#                 if deq.left:
#                     q.append(deq.left)

#                 if deq.right:
#                     q.append(deq.right)

#                 addq = deq
#             # res.append(visit)
            
#         # print(res)
#         return root