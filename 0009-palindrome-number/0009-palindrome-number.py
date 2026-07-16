class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palin=True
        Num=x
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x//=10
        if Num!=rev:
            is_palin=False
        return is_palin