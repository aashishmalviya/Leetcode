# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Morris inorder traversal, TC: O(N), SC: O(1)
#Ref: https://www.youtube.com/watch?v=wGXB9OWhPTg
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.currentNode = root

#     def next(self) -> int:
#         while self.currentNode:
#             if not self.currentNode.left:
#                 val = self.currentNode.val
#                 self.currentNode = self.currentNode.right
#                 return val

#             else:
#                 pred = self.currentNode.left

#                 while pred.right and pred.right != self.currentNode:
#                     pred = pred.right

#                 if pred.right == self.currentNode: #pred right is pointing to currentNode, link already exists
#                     pred.right = None
#                     val = self.currentNode.val
#                     self.currentNode = self.currentNode.right 
#                     return val
#                 else:
#                     pred.right = self.currentNode # link pred right to currentNode
#                     self.currentNode = self.currentNode.left


#     def hasNext(self) -> bool:
#         return self.currentNode is not None


#Ref : https://www.youtube.com/watch?v=D2jMcmxU4bs
#TC : Avg O(1), SC : O(H)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.curr = root
        self.pushLeftChilds(root)
    
    def pushLeftChilds(self, node : TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.pushLeftChilds(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()