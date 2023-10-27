class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        gasInTank = startingIndex = 0
        
        for i in range(len(gas)):
            gasInTank += gas[i] - cost[i]
            if(gasInTank < 0):
                gasInTank = 0
                startingIndex = i+1
        
        return startingIndex
        