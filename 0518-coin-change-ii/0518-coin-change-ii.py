# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [1] + [0] * amount
        
#         #coins.sort()
        
#         for currentCoin in coins:
#             for currentAmount in range(currentCoin, amount+1):
#                 dp[currentAmount] += dp[currentAmount - currentCoin]
                
#         return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def dfs_helper(index, amount):
            if index < 0 or amount < 0:
                return 0
            
            if (index, amount) in dp:
                return dp[(index, amount)]
            
            if amount == 0:
                return 1
            
            dp[(index, amount)] = dfs_helper(index, amount - coins[index]) + dfs_helper(index - 1, amount)
            return dp[(index, amount)]
        
        return dfs_helper(len(coins)-1, amount)