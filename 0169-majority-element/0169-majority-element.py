class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        vote=0
        for i in range(0,len(nums)):
            if vote==0:
                candidate=nums[i]
                vote=1
            elif candidate == nums[i]:
                vote+=1
            else:
                vote-=1
        return candidate
        