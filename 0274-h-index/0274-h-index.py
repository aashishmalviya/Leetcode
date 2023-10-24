class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citFreq = [0] * (n+1)
        
        for i, citRecvd in enumerate(citations):
            #print (i, citRecvd)
            if(citRecvd >= n):
                citFreq[n] += 1
            else:
                citFreq[citRecvd] += 1
        
        citCount = 0
        
        for i in range(n, -1, -1):
            citCount += citFreq[i]
            if(citCount >= i):
                return i;
            
        return -1
            