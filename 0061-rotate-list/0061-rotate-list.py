# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head
        listLen = 1
        
        while current.next:
            current = current.next
            listLen += 1
            
        current.next = head
        
        k = listLen - (k%listLen)
        
        while k>0:
            current = current.next
            k -= 1
        
        newHead = current.next
        
        current.next = None
        
        return newHead