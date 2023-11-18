class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * (amount)
        
        coins.sort()
        
        for currentAmount in range(1,amount+1):
            for coin in coins:
                if coin <= currentAmount:
                    dp[currentAmount] = min(dp[currentAmount], dp[currentAmount - coin] + 1)
                else:
                    break
        
        return dp[amount] if dp[amount] != amount+1 else -1