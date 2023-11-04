class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            test_sum = nums[left] + nums[right]
            
            if test_sum == target:
                return left+1, right+1
            
            elif test_sum < target:
                left += 1
                
            else:
                right -= 1
        
        return []