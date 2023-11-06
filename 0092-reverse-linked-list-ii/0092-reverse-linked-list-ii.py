# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummyNode = ListNode(0, head)
        prev = dummyNode
        
        for shifter in range(left - 1):
            prev = prev.next
            
        current = prev.next
        
        for neighbourtofront in range(right - left):
            
            nextNeighbour = current.next
            current.next = nextNeighbour.next
            nextNeighbour.next = prev.next
            prev.next = nextNeighbour
            
        return dummyNode.next