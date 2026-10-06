class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        max_len=0
        mapping={}
        while r<len(s):
            if s[r] in mapping:
                l=max(l,mapping[s[r]]+1)
            mapping[s[r]]=r
            max_len=max(max_len,(r-l)+1)
            r+=1
        return max_len