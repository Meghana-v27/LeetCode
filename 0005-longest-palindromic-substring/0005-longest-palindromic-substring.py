class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        start,end=0,0
        for i in range(len(s)):
            odd=ispalindrome(s,i,i)
            even=ispalindrome(s,i,i+1)
            length=max(odd,even)
            if length>(end-start):
                start=i-(length-1)//2
                end=i+length//2
        return s[start:end+1]