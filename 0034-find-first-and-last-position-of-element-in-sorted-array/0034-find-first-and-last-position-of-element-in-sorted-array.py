class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l1=0
        h1=len(nums)-1
        f=-1
        while l1<=h1:
            m1=(l1+h1)//2
            if nums[m1]==target:
                f=m1
                h1=m1-1
            elif nums[m1]<target:
                l1=m1+1
            else:
                h1=m1-1
        l2=0
        h2=len(nums)-1
        l=-1
        while l2<=h2:
            m2=(l2+h2)//2
            if nums[m2]==target:
                l=m2
                l2=m2+1
            elif nums[m2]<target:
                l2=m2+1
            else:
                h2=m2-1
        return [f,l]