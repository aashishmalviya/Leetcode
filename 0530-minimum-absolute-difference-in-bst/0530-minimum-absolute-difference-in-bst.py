# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def minabs_generator(root):
            if root:
                yield from minabs_generator(root.right)
                yield root.val
                yield from minabs_generator(root.left)
                
        test = list(starmap(operator.sub, pairwise(minabs_generator(root))))
        print(test)
        return min(test)