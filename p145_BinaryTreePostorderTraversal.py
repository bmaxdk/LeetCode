# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         stack, res = [(root, False)], []
        
#         while stack:
#             node, visit = stack.pop()
            
#             if visit:
#                 res.append(node.val)
                
#             else:
#                 stack.append((node, True))
#                 if node.right is not None:
#                     stack.append((node.right, False))
#                 if node.left is not None:
#                     stack.append((node.left, False))
#         return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []
        
        while stack:
            node, visit = stack.pop()
            if node:
                if visit:
                    res.append(node.val)

                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res