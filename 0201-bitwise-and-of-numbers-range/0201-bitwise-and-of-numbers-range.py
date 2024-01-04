# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/593317/Simple-3-line-Java-solution-faster-than-100
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/3220550/201%3A-Solution-with-step-by-step-explanation

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right-1
        return right