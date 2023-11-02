class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return reduce(xor, nums)
        return reduce(lambda a, b: a ^ b, nums)