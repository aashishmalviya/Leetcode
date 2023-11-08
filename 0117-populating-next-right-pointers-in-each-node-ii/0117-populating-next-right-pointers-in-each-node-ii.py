"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
            
        q = deque([root])
        
        while q:
            prev = None
            
            for _ in range(len(q)):
                currentNode = q.popleft()
                
                if prev:
                    prev.next = currentNode
                    
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
                    
                prev = currentNode
            
        return root 