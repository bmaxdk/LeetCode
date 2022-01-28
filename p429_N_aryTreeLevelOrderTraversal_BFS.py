# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, res = deque(), []
        if root:
            q.append(root)
        while len(q):
            visit = []
            for _ in range(len(q)):
                deq = q.popleft()
                visit.append(deq.val)
                for child in deq.children:
                    if child:
                        q.append(child)
            res.append(visit)
        return res