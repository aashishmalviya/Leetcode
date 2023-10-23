class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJumpFromHere = 0
        for i in range(0, len(nums)):
            if(i > maxJumpFromHere):
                return False
            maxJumpFromHere = max(maxJumpFromHere, i + nums[i])
        return True