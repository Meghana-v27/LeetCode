class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        left=[1]*len(nums)
        for i in range(0,len(nums)):
            left[i]=pre
            pre=pre*nums[i]
        suf=1
        right=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            right[i]=suf
            suf=suf*nums[i]
        res=[1]*len(nums)
        for i in range(0,len(nums)):
            res[i]=left[i]*right[i]
        return res