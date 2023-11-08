"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Solution using deque

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return None
            
#         q = deque([root])
        
#         while q:
#             prev = None
            
#             for _ in range(len(q)):
#                 currentNode = q.popleft()
                
#                 if prev:
#                     prev.next = currentNode
                    
#                 if currentNode.left:
#                     q.append(currentNode.left)
#                 if currentNode.right:
#                     q.append(currentNode.right)
                    
#                 prev = currentNode
            
#         return root 

#Solution using O(1) space:
# https://www.youtube.com/watch?v=UbhdyQ3albE

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        current = root
        
        while current:
            
            dummyNode = prev = Node(0)
            
            while current:
                if current.left:
                    prev.next = current.left
                    prev = prev.next

                if current.right:
                    prev.next = current.right
                    prev = prev.next

                current = current.next
            
            current = dummyNode.next
            
        return root