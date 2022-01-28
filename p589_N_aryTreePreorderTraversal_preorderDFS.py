# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# using Postorder DFS
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for i in range(len(node.children)):
                    stack.append(node.children[-(i+1)])
        return res