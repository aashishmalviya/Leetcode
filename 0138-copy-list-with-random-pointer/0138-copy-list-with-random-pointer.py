"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#ref : https://www.youtube.com/watch?v=byOMKHJezLE

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        current = head
        
        while current:
            temp = Node(current.val, current.next)
            current.next = temp
            current = temp.next
            
        current = head
        
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        original = head
        copy = head.next
        
        temp = copy
        
        while original.next and copy.next:
            original.next = original.next.next
            copy.next = copy.next.next
            
            original = original.next
            copy = copy.next
            
        return temp