# https://leetcode.com/problems/word-break/discuss/748479/Python3-Solution-with-a-Detailed-Explanation-Word-Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        Possible  = True

        max_word_len = len(max(wordDict, key=len))
        my_dict = set(wordDict)

        dp = [True] + [False] * n

        for current_len in range(1, n+1):
            for substr_index in range(current_len):
                if current_len - substr_index > max_word_len:
                    continue

                if dp[substr_index] == Possible and s[substr_index : current_len] in my_dict:
                    dp[current_len] = Possible
                    break

        return dp[n] == Possible