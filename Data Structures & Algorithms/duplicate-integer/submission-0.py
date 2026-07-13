class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            if (i in dict):
                dict[i]+=1
            else:
                dict[i]=1
        s=dict.values()
        for i in s:
            if i > 1:
                return True
        return False

        