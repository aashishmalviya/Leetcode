"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        old_to_copy = {}
        
        def cloner(old_node):
            if old_node in old_to_copy:
                return old_to_copy[old_node]
            
            copy_node = Node(old_node.val)
            
            old_to_copy[old_node] = copy_node
            
            for nbrs in old_node.neighbors:
                copy_node.neighbors.append(cloner(nbrs))
            
            return copy_node
        
        return cloner(node)