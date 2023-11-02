class Solution:
    def reverseBits(self, n: int) -> int:
        #return int(f'{n:032b}'[::-1], 2)
        return int(('{0:032b}'.format(n))[::-1], 2)