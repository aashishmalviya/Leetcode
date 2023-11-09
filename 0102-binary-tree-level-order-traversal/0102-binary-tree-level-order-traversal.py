# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        q = deque()
        q.append(root)
        
        while q:
            currentLevel = []
            
            for i in range(len(q)):
                currentNode = q.popleft()
                currentLevel.append(currentNode.val)
                
                if currentNode.left:
                    q.append(currentNode.left)
                    
                if currentNode.right:
                    q.append(currentNode.right)
                    
            if currentLevel:
                result.append(currentLevel)
        return result
                