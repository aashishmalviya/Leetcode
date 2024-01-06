class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        def expand_middle(l, r) -> str:
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1 : r]
    
        for i in range(len(s)):
            res = max(expand_middle(i,i), expand_middle(i,i+1), res, key = len)
        
        return res        
            
                