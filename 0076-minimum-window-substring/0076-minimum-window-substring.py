from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)

        result = ""
        required = defaultdict(int)

        matched_chars = 0

        start, end = 0, 0
        min_length = float('inf')

        for c in t:
            required[c] += 1

        while end < slen:
            if s[end] in required:
                if required[s[end]] > 0:
                    matched_chars += 1
                    
            required[s[end]] -= 1 
            
            end += 1

            while matched_chars == tlen:
                if end - start < min_length:
                    min_length = end - start
                    result = s[start : end]

                required[s[start]] += 1
                if required[s[start]] > 0:
                    matched_chars -= 1

                start += 1


        return result

