class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float('inf')
        maxProfitTillNow = 0
        for currentPrice in prices:
            if(currentPrice < minValue):
                minValue = currentPrice
                
            maxProfitTillNow = max(maxProfitTillNow, currentPrice - minValue)
        
        return maxProfitTillNow