# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        if nums[low] < nums[high]:
            return nums[low]
        
        while low < high:
            mid = (low + high) >> 1
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            
        #print (low, high)
        return nums[low]