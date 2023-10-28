class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        n = len(nums)
        
        for i in range(0, n-2):
            
            if nums[i] > 0:
                break
            
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            j = i+1
            k = n-1
            
            while(j < k):
                currentSum = nums[i] + nums[j] + nums[k]
                
                if(currentSum < 0):
                    j += 1
                elif (currentSum > 0):
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while k>j and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
         
        
        return res