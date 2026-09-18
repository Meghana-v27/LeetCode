class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set=set(nums)
        max_length=1
        for i in nums_set:
            if i-1 not in nums_set:
                curr=i
                length=1
                while curr+1 in nums_set:
                    length+=1
                    curr+=1
                if length>max_length:
                    max_length=length
        return max_length