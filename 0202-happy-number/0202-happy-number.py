class Solution:
    def digSquareSum(self, n:int) -> int:
        finalSum = 0
        while n > 0:
            dig = n % 10
            finalSum += dig * dig
            n //= 10
        return finalSum
    
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        
        slow = self.digSquareSum(slow)
        fast = self.digSquareSum(self.digSquareSum(fast))

        while slow!=1 and slow!=fast:
            slow = self.digSquareSum(slow)
            fast = self.digSquareSum(self.digSquareSum(fast))
            
        return fast == 1