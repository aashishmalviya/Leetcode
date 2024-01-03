# https://www.youtube.com/watch?v=7xJJ_42P_0U
# https://www.youtube.com/watch?v=MInz2ao4wao

class Solution:
	def singleNumber(self, nums: list[int]) -> int:
		if not nums:
		    return 0
		   
		ones, twos = 0, 0
		for num in nums:
			ones = (ones ^ num) & (~twos)
			twos = (twos ^ num) & (~ones)
		return ones

# 	def testSol(self):
# 		assert self.singleNumber([2, 2, 3, 2]) == 3
# 		assert self.singleNumber([]) == 0
# 		assert self.singleNumber(None) == 0
# 		print("All ok")

# test = Solution()
# test.testSol()
# print(test.singleNumber([2, 2, 3, 2]))