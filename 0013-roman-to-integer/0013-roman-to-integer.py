class Solution:
    def romanToInt(self, s: str) -> int:
        romanIntMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        ans = 0
        for i in range(len(s)-1):
            if romanIntMap[s[i]] < romanIntMap[s[i+1]]:
                ans -= romanIntMap[s[i]]
            else:
                ans += romanIntMap[s[i]]
                
        ans += romanIntMap[s[-1]]
        
        return ans