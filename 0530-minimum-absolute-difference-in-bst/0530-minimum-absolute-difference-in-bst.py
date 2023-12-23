# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_diff = 1e9
        self.prev_node = None
            
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inorder(node):
            
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev_node:
                self.min_diff = min(self.min_diff, node.val - self.prev_node.val)
            
            self.prev_node = node
            
            inorder(node.right)
        
        
        inorder(root)
        return int(self.min_diff)