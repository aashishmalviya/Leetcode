# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/sort-list/discuss/3206790/148%3A-Solution-with-step-by-step-explanation
# https://leetcode.com/problems/sort-list/discuss/1796085/Sort-List-or-Python-O(nlogn)-Solution-or-95-Faster

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def get_mid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge_sorted_lists(left, right) -> ListNode:
            dummy_node = ListNode(0)
            current = dummy_node

            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                
                else:
                    current.next = right
                    right = right.next

                current = current.next

            current.next = left or right
            return dummy_node.next

        mid = get_mid(head)

        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return merge_sorted_lists(left, right)