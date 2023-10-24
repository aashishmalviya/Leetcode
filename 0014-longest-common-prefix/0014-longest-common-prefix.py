class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestString = min(strs, key=len)
        
        for item in strs:
            while len(shortestString) > 0:
                if item.startswith(shortestString):
                    break
                else:
                    shortestString = shortestString[:-1]
        
        return shortestString