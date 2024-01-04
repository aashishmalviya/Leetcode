# https://leetcode.com/problems/word-break/discuss/748479/Python3-Solution-with-a-Detailed-Explanation-Word-Break

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)

#         Possible  = True

#         max_word_len = len(max(wordDict, key=len))
#         my_dict = set(wordDict)

#         dp = [True] + [False] * n

#         for current_len in range(1, n+1):
#             for substr_index in range(current_len):
#                 if current_len - substr_index > max_word_len:
#                     continue

#                 if dp[substr_index] == Possible and s[substr_index : current_len] in my_dict:
#                     dp[current_len] = Possible
#                     break

#         return dp[n] == Possible

class Solution:
    def __init__(self):
        self.wordSet = set()
        self.dp_len = None

    def dfs_helper(self, index: int, s: str) -> bool:
        if index == len(s):
            return True

        if self.dp_len[index] != -1:
            return self.dp_len[index]
        
        if s in self.wordSet:
            return True

        prefix = ""
        
        for i in range(index, len(s)):
            prefix += s[i]
            #print(prefix)
            if prefix in self.wordSet and self.dfs_helper(i+1, s):
                self.dp_len[index] = True
                return self.dp_len[index]

        self.dp_len[index] = False
        return self.dp_len[index]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        self.dp_len = [-1] * (len(s) + 1)
        print(self.wordSet)
        return self.dfs_helper(0, s)