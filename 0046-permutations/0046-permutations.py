class Solution:
    def permutation_helper(self, nums, final_result, current_res):
        if not nums:
            final_result.append(current_res)
            return

        for i in range(len(nums)):
            self.permutation_helper(nums[:i] + nums[i+1:], final_result, current_res + [nums[i]])

    def permute(self, nums: List[int]) -> List[List[int]]:
        final_result = []
        self.permutation_helper(nums, final_result, [])
        return final_result