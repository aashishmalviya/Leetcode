class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lmax, rmax = 0, len(height)-1, height[0], height[len(height) - 1]
        
        total_water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    total_water += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    total_water += rmax - height[r]
                r -= 1
                
        return total_water