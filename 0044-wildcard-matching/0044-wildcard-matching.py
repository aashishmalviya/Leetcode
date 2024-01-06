class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def solver(i, j) -> bool:
            if i<0 and j<0: return True

            if i>=0 and j<0: return False

            if i<0 and j>=0:
                for k in range(0, j+1):
                    if p[k] != '*':
                        return False
                return True

            if s[i] == p[j] or p[j] == '?':
                return solver(i-1, j-1)
            elif p[j] == '*':
                return solver(i, j-1) or solver(i-1, j)
            else:
                return False

        return solver(len(s)-1, len(p)-1)