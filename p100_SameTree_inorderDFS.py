# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# pre-orderDFS
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         stack1, out1 = [p], []
#         stack2, out2 = [q], []
#         req = True
#         #here try with preorder DFS
#         while stack1 and stack2:
#             tree1 = stack1.pop()
#             tree2 = stack2.pop()
#             if tree1 and tree2:
#                 if tree1.val != tree2.val:
#                     return False
#                 stack1.append(tree1.right)
#                 stack2.append(tree2.right)
#                 stack1.append(tree1.left)
#                 stack2.append(tree2.left)
#             if tree1 is None and tree2 is not None:
#                 return False
#             if tree1 is not None and tree2 is None:
#                 return False
#         return True

# inorderDFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack, req = [p], []
        stack2, req2 = [q], []
        
        while stack and stack2:
            node = stack.pop()
            node2 = stack2.pop()
            if node and node2:
                if node.val != node2.val:
                    return False
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
                
                stack2.append(node2.right)
                stack2.append(node2)
                stack2.append(node2.left)
            else:
                if node is None and node2 is not None:
                    return False
                if node is not None and node2 is None:
                    return False
                if len(stack) == 0 and len(stack2) == 0: # this condition for next node 
                    break
                node = stack.pop()
                node2 = stack2.pop()

        return True
                