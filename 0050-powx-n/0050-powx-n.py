class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        p = abs(n)

        while p>0:
            if p&1: #odd power
                res = res*x
            x = x*x
            p >>= 1

        return 1.0/res if n<0 else res