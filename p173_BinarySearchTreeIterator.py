# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.res =self.inorderDFS()
        self.size = len(self.res)
        self.count = 0
        
    def next(self) -> int:
        val = self.res[self.count]
        self.count+=1
        return val

    def hasNext(self) -> bool:
        return self.count < self.size
    
    def inorderDFS(self):
        stack, res = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                res.append(node.val)
        return res

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

