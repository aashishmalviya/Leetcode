class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_of_char = {}
        
        l, max_win_size = 0, 0
        
        for r in range(len(s)):
            
            current_char = s[r]
            
            if current_char in index_of_char and index_of_char[current_char] >= l:
                l = index_of_char[current_char] + 1
            else:
                max_win_size = max(max_win_size, (r - l) + 1)
                
            index_of_char[current_char] = r
        
        return max_win_size