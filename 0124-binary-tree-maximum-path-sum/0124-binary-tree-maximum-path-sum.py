# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path_sum = float('-inf')

    def depth(self, root : TreeNode) -> int:
        if not root:
            return float('-inf')

        left = max(0, self.depth(root.left))
        right = max(0, self.depth(root.right))

        if (root.val + left + right) > self.max_path_sum:
            self.max_path_sum = (root.val + left + right)

        return root.val + max(left, right)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_path_sum