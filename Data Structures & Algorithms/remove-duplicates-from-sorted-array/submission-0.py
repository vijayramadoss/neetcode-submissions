class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=1
        n=len(nums)
        count=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                nums[idx]=nums[i]
                idx+=1
        return n-count
