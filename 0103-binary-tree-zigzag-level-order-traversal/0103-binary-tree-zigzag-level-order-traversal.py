# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        zigzagLevel = False
        
        result, currentLevel = [], [root]
        
        while currentLevel:
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                    
            if zigzagLevel:
                currentLevel.reverse()
                zigzagLevel = False
            else:
                zigzagLevel = True

            result.append([i.val for i in currentLevel])
            currentLevel = nextLevel
                
        return result
                