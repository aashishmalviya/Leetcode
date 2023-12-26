# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/3066073/One-Pass-or-Java-or-python-or-C%2B%2B-Simple-and-Short-Explained-Solution

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        max_sum, min_sum = nums[0], nums[0]
        cur_max, cur_min = 0, 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(cur_max, max_sum)

            cur_min = min(cur_min + num, num)
            min_sum = min(cur_min, min_sum)

        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum

        