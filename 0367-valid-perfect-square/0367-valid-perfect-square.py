class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l=0
        h=num
        while l<=h:
            m=(l+h)//2
            if (m*m)==num:
                return True
            elif m*m<num:
                l=m+1
            else:
                h=m-1
        return False