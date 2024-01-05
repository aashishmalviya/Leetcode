# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
        
#         dp = [1] * n
        
#         for i in range(n-1):
#             for j in range(i+1, n):
                
#                 if nums[j] > nums[i]:
#                     dp[j] = max(1 + dp[i], dp[j])
                    
#         return max(dp)


#https://leetcode.com/problems/longest-increasing-subsequence/discuss/2395570/Python3-oror-7-lines-binSearch-cheating-wexplanation-oror-TS%3A-98-100

# TC: NlogN, SC: N
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums.pop(0)]

        for n in nums:
            if n > res[-1]:
                res.append(n)
            else:
                res[bisect_left(res, n)] = n

        return len(res)