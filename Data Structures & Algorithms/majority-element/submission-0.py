class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for i in range(len(nums)):
            s[nums[i]]=s.get(nums[i],0)+1
        l=list(s.items())
        for i,j in l:
            if j>len(nums)/2:
                return i