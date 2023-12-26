# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None

#         def merge_sorted_lists(left, right) -> ListNode:
#             if not left:
#                 return right
#             if not right:
#                 return left
        
#             if left.val < right.val:
#                 left.next = merge_sorted_lists(left.next, right)
#                 return left
#             else:
#                 right.next = merge_sorted_lists(left, right.next)
#                 return right

#         lists_count = len(lists)
#         #top_list = lists[0]
#         for i in range(1, lists_count):
#             lists[0] = merge_sorted_lists(lists[0], lists[i])

#         return lists[0]

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        nodes_vals = []

        for head_in_current_list in lists:
            while head_in_current_list:
                nodes_vals += [head_in_current_list.val]
                head_in_current_list = head_in_current_list.next

        
        nodes_vals.sort(reverse = True)
        print(nodes_vals)
        
        list_head = None

        for current_node_val in nodes_vals:
            list_head = ListNode(current_node_val, list_head)

        return list_head