class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        res=0
        while l<=h:
            m=(l+h)//2
            sq=m*m
            if sq<=x:
                res=m
                l=m+1
            else:
                h=m-1
        return res