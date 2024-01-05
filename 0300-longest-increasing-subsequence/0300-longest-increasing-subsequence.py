class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(n-1):
            for j in range(i+1, n):
                
                if nums[j] > nums[i]:
                    dp[j] = max(1 + dp[i], dp[j])
                    
        return max(dp)