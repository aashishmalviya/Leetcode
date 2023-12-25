class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        final_result = []
        n = len(candidates)
        
        def helper(current_sum, current_list, index):
            if current_sum > target:
                return

            if current_sum == target:
                final_result.append(current_list)
                return
            
            for i in range(index, n):
                helper(current_sum + candidates[i], current_list + [candidates[i]], i)
        
        helper(0, [], 0)
        return final_result
        