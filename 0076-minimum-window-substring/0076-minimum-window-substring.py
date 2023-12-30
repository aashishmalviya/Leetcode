from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)

        result = ""
        tmap = defaultdict(int)
        window = defaultdict(int)
        matched_keys = 0
        required_keys = 0

        start, end = 0, 0
        min_length = float('inf')

        for c in t:
            tmap[c] += 1

        required_keys = len(tmap)

        left = 0
        for right, current_char in enumerate(s):
            window[current_char] += 1

            if window[current_char] == tmap[current_char]:
                matched_keys += 1

            while matched_keys == required_keys:
                if min_length > (right + 1 - left):
                    result = s[left : right + 1]
                    min_length = (right + 1 - left)

                window[s[left]] -= 1
                if s[left] in tmap and window[s[left]] < tmap[s[left]]:
                    matched_keys -= 1

                left += 1

        return result
