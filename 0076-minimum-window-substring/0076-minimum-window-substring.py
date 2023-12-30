#https://leetcode.com/problems/minimum-window-substring/discuss/304161/Python3-sliding-window

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        required_map_len = len(t_map)
        current_map_len = 0
        window_map = Counter()
        min_length = float('inf')
        final_result = ""
        start = 0

        for end, current_char in enumerate(s):
            if current_char in t_map:
                window_map[current_char] += 1
                if window_map[current_char] == t_map[current_char]:
                    current_map_len += 1

            while current_map_len == required_map_len:
                if (end - start + 1) < min_length:
                    min_length = (end - start + 1)
                    final_result = s[start: end + 1]

                if s[start] in t_map:
                    window_map[s[start]] -= 1
                    if window_map[s[start]] < t_map[s[start]]:
                        current_map_len -= 1

                start += 1

        return final_result
