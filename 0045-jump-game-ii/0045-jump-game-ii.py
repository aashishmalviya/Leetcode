class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = totalJumps = 0
        while (r < len(nums) - 1):
            totalJumps += 1
            longestJump = max([i + nums[i] for i in range(l,r+1)])
            l, r = r+1, longestJump
            
        return totalJumps
            