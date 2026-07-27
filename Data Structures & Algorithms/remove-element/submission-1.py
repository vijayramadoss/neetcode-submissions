class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx=0
        count=0
        n=len(nums)
        for i in nums:
            if i !=val:
                nums[idx]=i
                idx+=1
                count+=1
        return count