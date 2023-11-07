# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def dfs(self, root: TreeNode, currentVal: int) -> None:
        if not root:
            return
        
        sumTillCurrentNode = (currentVal*10 + root.val)
        
        if not root.left and not root.right:
            self.sum += sumTillCurrentNode
            return
        
        self.dfs(root.left, sumTillCurrentNode)
        self.dfs(root.right, sumTillCurrentNode)
    
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.sum