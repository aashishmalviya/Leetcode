# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     smallNodeCounter = 0
#     ansFound = False
#     ans = None
    
#     def solver(self, root, k):
#         if root == None or self.ansFound == True:
#             return
        
#         self.solver(root.left, k)
        
#         self.smallNodeCounter += 1
        
#         if self.smallNodeCounter == k:
#             self.ansFound = True
#             self.ans = root.val
#             return
        
#         self.solver(root.right, k)
        
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.solver(root, k)
#         return self.ans


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for i, node in enumerate(self.helper(root), 1):
            if i == k:
                return node.val
            
    def helper(self, root) -> Generator:
        if root:
            yield from self.helper(root.left)
            yield root
            yield from self.helper(root.right)
    