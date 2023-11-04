class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_water_contained = 0, len(height) - 1, 0
        
        while l < r:
            current_container_capacity = (r - l) * min(height[l], height[r])
            
            max_water_contained = max(max_water_contained, current_container_capacity)
            
            if height[l] < height[r]:
                l += 1
            else :
                r -= 1
        
        return max_water_contained