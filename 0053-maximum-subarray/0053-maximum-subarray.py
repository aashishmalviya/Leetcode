class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sum = max(cur_sum, max_sum)

        return max_sum