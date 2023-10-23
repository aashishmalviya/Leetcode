class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElementCounter = 0
        majElement = nums[0]
        
        for i in range(0, len(nums)):
            if(nums[i] == majElement):
                majElementCounter += 1
                
            elif(majElementCounter == 0):
                majElement = nums[i]
                majElementCounter = 1
                
            else:
                majElementCounter -= 1
        
        return majElement