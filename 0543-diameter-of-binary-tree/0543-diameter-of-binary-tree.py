# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if self.diameter < (left + right):
            self.diameter = (left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter
