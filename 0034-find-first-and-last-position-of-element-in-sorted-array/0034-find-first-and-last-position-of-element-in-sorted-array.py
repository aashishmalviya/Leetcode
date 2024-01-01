class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        return [left, right-1] if left != right else [-1, -1]