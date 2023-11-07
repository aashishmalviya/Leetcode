class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        myDict = set(wordDict)
        
        dp = [True] + [False] * n
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] == True:
                    if s[j:i] in myDict:
                        dp[i] = True
                        break
        
        return dp[n] == True