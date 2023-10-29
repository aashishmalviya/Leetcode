class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffHash = {}
        
        for index,num in enumerate(nums):
            diff = target - num
            if diff in diffHash:
                return [diffHash[diff], index]
            
            diffHash[num] = index