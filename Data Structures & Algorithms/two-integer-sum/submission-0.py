class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in (range(len(nums))):
           if nums[i] not in s:
                s[nums[i]]=i
        for i in range(len(nums)):
            k=target-nums[i]
            if k in s and s[k] != i:
                if s[k]<i:
                   return [s[k],i]
                else:
                    return [i,s[k]]
        return []


        