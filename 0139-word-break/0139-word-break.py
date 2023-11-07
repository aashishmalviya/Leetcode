# https://leetcode.com/problems/word-break/discuss/748479/Python3-Solution-with-a-Detailed-Explanation-Word-Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        maxLen = len(max(wordDict, key = len))
        
        myDict = set(wordDict)
        
        dp = [True] + [False] * n
        
        for i in range(1, n+1):
            for j in range(i):
                if i-j > maxLen:
                    continue
                    
                if dp[j] == True:
                    if s[j:i] in myDict:
                        dp[i] = True
                        break
        
        return dp[n] == True