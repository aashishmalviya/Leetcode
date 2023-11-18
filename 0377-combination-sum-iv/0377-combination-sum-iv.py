class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * (target+1)
        
        nums.sort()
        
        for currentTarget in range(1, target+1):
            for currentNum in nums:
                if currentNum <= currentTarget:
                    dp[currentTarget] = (dp[currentTarget] + dp[currentTarget - currentNum])
                else:
                    break
                    
        return dp[target]