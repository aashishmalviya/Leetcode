class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        
        merged = []
        
        for current_interval in intervals:
            if not merged or merged[-1][1] < current_interval[0]:
                merged.append(current_interval)
            else:
                merged[-1][1] = max(merged[-1][1], current_interval[1])
        
        return merged