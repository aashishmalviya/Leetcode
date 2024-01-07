class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        #print(dp)
        
        # @cache
        def dfs_helper(i, j) -> int:
            if i == 0:
                return j
            
            if j == 0:
                return i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dfs_helper(i-1, j-1)
                return dp[i][j]

            dp[i][j] = 1 + min(dfs_helper(i-1,j), dfs_helper(i,j-1), dfs_helper(i-1,j-1))
            return dp[i][j]

        return dfs_helper(len(word1), len(word2))