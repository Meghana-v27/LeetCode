class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        low=1
        high=n-2
        while low<=high:
            m=(low+high)//2
            if nums[m]>nums[m+1] and nums[m]>nums[m-1]:
                return m
            elif nums[m+1]>nums[m]:
                low=m+1
            else:
                high=m-1
        return -1
