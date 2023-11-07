# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, next = head)
        
        while prev.next and prev.next.next:
            current = prev.next
            
            if current.val != current.next.val:
                prev = current
                continue
                
            while current and prev.next.val == current.val:
                current = current.next
            
            prev.next = current
        
        return dummy.next