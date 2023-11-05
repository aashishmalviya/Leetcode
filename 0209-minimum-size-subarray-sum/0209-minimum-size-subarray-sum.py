class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, min_win_size, current_sum = 0, 0, float('inf'), 0
        
        
        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum >= target:
                min_win_size = min(min_win_size, (r - l) + 1)
                current_sum -= nums[l]
                l += 1
                
        return 0 if min_win_size == float('inf') else min_win_size