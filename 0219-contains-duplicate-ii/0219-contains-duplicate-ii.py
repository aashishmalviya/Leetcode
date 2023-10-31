class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(set(nums)) == len(nums):
            return False
        
        window = set()
        
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if(len(window)) == k+1 : window.remove(nums[i-k])
        
        return False