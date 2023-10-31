# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1
        
        while l1 or l2:
            if not l1.next and l2:
                l1.next, l2.next = l2.next, l1.next
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            carry, l1.val = divmod(val1 + val2 + carry, 10)
            
            tail = l1
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry:
            tail.next = ListNode(carry)
            
        return head