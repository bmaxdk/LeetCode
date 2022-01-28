# 1305. All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst = self.dfs(root1) + self.dfs(root2)
        return sorted(lst)
        
    def dfs(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            # print(node.val)
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res