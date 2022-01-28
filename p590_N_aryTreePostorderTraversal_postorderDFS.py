# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# using Postorder DFS
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, res = [(root, False)], []
        while stack:
            node, visit = stack.pop()
            if node:
                if visit:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    for i in range(len(node.children)):
                        stack.append((node.children[-(i+1)], False))
                    
        return res
                
                