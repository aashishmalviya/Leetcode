class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_db = set(nums)
        max_sequence_length = 0
        
        while nums_db:
            
            low = high = nums_db.pop()
            
            while low-1 in nums_db or high+1 in nums_db:
                
                if low-1 in nums_db:
                    nums_db.remove(low-1)
                    low -= 1
                
                if high+1 in nums_db:
                    nums_db.remove(high+1)
                    high += 1
                    
            max_sequence_length = max(max_sequence_length, high - low + 1)
                
        return max_sequence_length
        