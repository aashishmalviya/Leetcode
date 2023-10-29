class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rangeList = []
        
        for n in nums:
            if rangeList and rangeList[-1][1] == n-1:
                rangeList[-1][1] = n
            else:
                rangeList.append([n,n])
        
        return [f'{x}->{y}' if x!=y else f'{x}' for x,y in rangeList ]