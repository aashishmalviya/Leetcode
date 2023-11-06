class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for current_interval in intervals:
            if current_interval[1] < newInterval[0] :
                result.append(current_interval)
                
            elif newInterval[1] < current_interval[0] :
                result.append(newInterval)
                newInterval = current_interval
            
            elif current_interval[1] > newInterval[0] or current_interval[0] < newInterval[1]:
                newInterval[0] = min(newInterval[0], current_interval[0])
                newInterval[1] = max(newInterval[1], current_interval[1])
            
        result.append(newInterval)
        return result