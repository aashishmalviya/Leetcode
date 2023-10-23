class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitPossible = 0
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):
                maxProfitPossible += (prices[i] - prices[i-1])
            
        return maxProfitPossible