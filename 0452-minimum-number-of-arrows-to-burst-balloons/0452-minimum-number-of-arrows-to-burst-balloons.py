#ref: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/3000422/Python-3-oror-7-lines-w-explanation-and-example-oror-TM%3A-98-92

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[1]))
        
        min_arrow_count = 1
        
        arrow_prev_position = points[0][1]
        
        for start, end in points:
            if arrow_prev_position < start:
                arrow_prev_position = end
                min_arrow_count += 1
        
        return min_arrow_count
        