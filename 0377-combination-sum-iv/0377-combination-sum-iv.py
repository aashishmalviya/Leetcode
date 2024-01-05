# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [1] + [0] * (target+1)
        
#         nums.sort()
        
#         for currentTarget in range(1, target+1):
#             for currentNum in nums:
#                 if currentNum <= currentTarget:
#                     dp[currentTarget] = (dp[currentTarget] + dp[currentTarget - currentNum])
#                 else:
#                     break
                    
#         return dp[target]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = collections.defaultdict(int)
        dp[0] = 1
        def dfs_helper(current_target) -> int:
            if current_target < 0:
                return 0
            
            if current_target in dp:
                return dp[current_target]
            
            if current_target == 0:
                return 1
            
            res = 0
            for n in nums:
                if current_target < n:
                    break
                res += dfs_helper(current_target - n)
            dp[current_target] = res
            return res
        
        #print(dp.items())
        #return dp[target]
        nums.sort()
        return dfs_helper(target)