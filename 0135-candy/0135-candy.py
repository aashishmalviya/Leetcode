class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        totalCandies = len(ratings)
        i = 1
        
        while i < len(ratings):
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            peak = 0
            while i < len(ratings) and ratings[i] > ratings[i-1]:
                peak += 1
                totalCandies += peak
                i += 1
            
            if i == len(ratings):
                return totalCandies
            
            valley = 0
            while i < len(ratings) and ratings[i] < ratings[i-1]:
                valley += 1
                totalCandies += valley
                i += 1
            
            totalCandies -= min(peak, valley)
            
        return totalCandies