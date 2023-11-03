class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return n
        
        total_ways = 0
        way_1, way_2 = 1, 1
        
        for i in range(1, n):
            total_ways = way_1 + way_2
            way_1 = way_2
            way_2 = total_ways
        
        return total_ways