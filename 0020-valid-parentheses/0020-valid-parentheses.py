class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = dict(('()', '{}', '[]'))
        
        stack = []
        
        for c in s:
            if c not in bracketDict:
                if not stack or c!=bracketDict[stack.pop()]:
                    return False
            else:
                stack.append(c)
        
        return len(stack)==0