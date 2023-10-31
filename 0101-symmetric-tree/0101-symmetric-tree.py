# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_mirror_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.is_mirror_tree(p.left, q.right) and self.is_mirror_tree(p.right, q.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror_tree(root.left, root.right)