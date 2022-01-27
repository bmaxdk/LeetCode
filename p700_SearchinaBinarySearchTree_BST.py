# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None or root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

#using DFS
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val == val:
#                     return node
#                 elif node.val < val:
#                     stack.append(node.right)
#                 else:
#                     stack.append(node.left)
#         return 
#     -------------------------------------------------------------------
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val == val:
#                     return node
#                 stack.append(node.right)
#                 stack.append(node.left)
#         return 
    
    
    
# bottom provide same but return type is different so rejected
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         stack, res = [root], []
#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val == val:
#                     res.append(node.val)
#                     if node.left:
#                         res.append(node.left.val)
#                     if node.right:
#                         res.append(node.right.val)
#                     break
#                 stack.append(node.right)
#                 stack.append(node.left)
#         return res