from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        @cache
        def my_gcd(a, b):
            while b:
                a, b = b, a%b
            return abs(a)

        points.sort()

        slopes_map, max_frequency_of_slopes = defaultdict(int), 0

        for current_index, (x1, y1) in enumerate(points):

            slopes_map.clear()

            for x2, y2 in points[current_index+1 : ]:
                dx = x2 - x1
                dy = y2 - y1

                G = my_gcd(dx, dy)

                current_slope = (dx//G, dy//G)

                slopes_map[current_slope] += 1
                max_frequency_of_slopes = max(max_frequency_of_slopes, slopes_map[current_slope])


        return max_frequency_of_slopes + 1


