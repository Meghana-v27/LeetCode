class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        rev_res=''
        for ch in s:
            if 'A'<=ch<='Z' or 'a'<=ch<='z':
                if 'A'<=ch<='Z':
                    res+=chr(ord(ch)+32)
                else:
                    res+=ch
            elif '0'<=ch<='9':
                res+=ch
        for ch in res:
            rev_res=ch+rev_res
        if res==rev_res:
            return True
        else:
            return False