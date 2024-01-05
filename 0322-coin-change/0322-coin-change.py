# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [0] + [amount+1] * (amount)
        
#         coins.sort()
        
#         for currentAmount in range(1,amount+1):
#             for coin in coins:
#                 if coin <= currentAmount:
#                     dp[currentAmount] = min(dp[currentAmount], dp[currentAmount - coin] + 1)
#                 else:
#                     break
        
#         return dp[amount] if dp[amount] != amount+1 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs_helper(index, amount):
            if index < 0 or amount < 0:
                return 1e9
            
            if (index, amount) in dp:
                return dp[(index, amount)]
            
            if amount == 0:
                return 0
            
            dp[(index, amount)] = min(1 + dfs_helper(index, amount - coins[index]), dfs_helper(index-1, amount))
            return dp[(index, amount)]
        
        ans = dfs_helper(len(coins)-1, amount)
        return ans if ans!= 1e9 else -1