# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = bisect_left(nums, target)
#         right = bisect_right(nums, target)        
#         return [left, right-1] if left != right else [-1, -1]

# https://www.youtube.com/watch?v=4sQL7R5ySUU
class Solution:
    def bin_search(self, nums, target, left_aligned):
        left, right = 0, len(nums)-1

        index = -1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                index = mid
                if left_aligned:
                    right = mid - 1
                else:
                    left = mid + 1

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bin_search(nums, target, True)
        right = self.bin_search(nums, target, False)
        return [left, right]