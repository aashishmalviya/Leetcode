class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        
        coins.sort()
        
        for currentCoin in coins:
            for currentAmount in range(currentCoin, amount+1):
                dp[currentAmount] += dp[currentAmount - currentCoin]
                
        return dp[amount]