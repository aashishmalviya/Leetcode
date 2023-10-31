# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        result_list = []
        
        while q:
            qlen = len(q)
            levelsum = 0
            for i in range(qlen):
                node = q.popleft()
                levelsum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result_list.append(levelsum/qlen)
        return result_list
                