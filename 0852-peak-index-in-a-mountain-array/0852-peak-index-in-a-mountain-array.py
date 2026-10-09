class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l=0
        h=len(arr)-1
        while l<=h:
            m=(l+h)//2
            if arr[m]>arr[m+1] and arr[m]>arr[m-1]:
                return m
            elif arr[m+1]>arr[m]:
                l=m+1
            else:
                h=m-1