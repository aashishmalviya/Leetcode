class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJumpFromHere = 0
        totalJumps = 0
        prevJump = 0
        
        for i in range(0, len(nums) - 1):
            maxJumpFromHere = max(maxJumpFromHere, i + nums[i])
            
            if(i == prevJump):
                totalJumps += 1
                prevJump = maxJumpFromHere
                
        return totalJumps
            


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         l = r = totalJumps = 0
#         while (r < len(nums) - 1):
#             totalJumps += 1
#             longestJump = max([i + nums[i] for i in range(l,r+1)])
#             l, r = r+1, longestJump
            
#         return totalJumps
            