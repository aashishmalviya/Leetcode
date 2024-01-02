import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]

        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def swap(lst, a, b):
#             lst[a], lst[b] = lst[b], lst[a]

#         n = len(nums)

#         def partition(start, end):
#             pivot_element = nums[end]

#             pivot_index = start - 1

#             for i in range(start, end):
#                 if nums[i] < pivot_element:
#                     pivot_index += 1
#                     swap(nums, i, pivot_index)

#             swap(nums, pivot_index + 1, end)
#             return pivot_index + 1

#         def quick_select(start, end):
#             if start < end:
#                 pivot_index = partition(start, end)

#                 if pivot_index == n-k:
#                     return nums[pivot_index]

#                 elif pivot_index > (n-k):
#                     return quick_select(start, pivot_index - 1)

#                 else:
#                     return quick_select(pivot_index + 1, end)

#             return nums[start]

#         return quick_select(0, n-1)