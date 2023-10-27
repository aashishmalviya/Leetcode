class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                    
                if j == len(needle)-1:
                    return i
                
        return -1
                