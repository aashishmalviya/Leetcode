# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        self.node_count = 0
        
    def helper(self, node: TreeNode, k: int):
        if not node or self.node_count>k:
            return
        
        self.helper(node.left, k)
        
        self.node_count += 1
        
        if self.node_count == k:
            self.result = node.val
            return
        
        self.helper(node.right, k)
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.helper(root, k)
        return self.result