class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        k=s.items()
        for i,j in k:
            if j==1:
                return i