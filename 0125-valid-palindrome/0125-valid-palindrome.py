class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = [i for i in s.lower() if i.isalnum()]
        return newStr == newStr[::-1]